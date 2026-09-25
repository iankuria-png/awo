# Composite a screenshot into a phone photo with a hand-measured screen quad.
import sys, numpy as np
from PIL import Image, ImageFilter, ImageDraw
photo_p, shot_p, out_p, quad_s = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
radius = int(sys.argv[5]) if len(sys.argv) > 5 else 90
quad = [tuple(map(float, p.split(','))) for p in quad_s.split(';')]  # TL;TR;BR;BL
photo = Image.open(photo_p).convert('RGB')
L = np.asarray(photo.convert('L')).astype(int)
qw = (np.hypot(quad[1][0] - quad[0][0], quad[1][1] - quad[0][1]) + np.hypot(quad[2][0] - quad[3][0], quad[2][1] - quad[3][1])) / 2
qh = (np.hypot(quad[3][0] - quad[0][0], quad[3][1] - quad[0][1]) + np.hypot(quad[2][0] - quad[1][0], quad[2][1] - quad[1][1])) / 2
shot = Image.open(shot_p).convert('RGB')
W = shot.width; H = int(round(W * qh / qw))
shot = shot.crop((0, 0, W, min(H, shot.height)))
W, H = shot.size
src = [(0, 0), (W, 0), (W, H), (0, H)]
A = []; B = []
for (X, Y), (u, v) in zip(quad, src):
    A.append([X, Y, 1, 0, 0, 0, -u * X, -u * Y]); B.append(u)
    A.append([0, 0, 0, X, Y, 1, -v * X, -v * Y]); B.append(v)
coef = tuple(np.linalg.solve(np.array(A, float), np.array(B, float)))
warped = shot.transform(photo.size, Image.PERSPECTIVE, coef, Image.BICUBIC)
rmask = Image.new('L', (W, H), 0); ImageDraw.Draw(rmask).rounded_rectangle((0, 0, W - 1, H - 1), radius=radius, fill=255)
wmask = rmask.transform(photo.size, Image.PERSPECTIVE, coef, Image.BICUBIC).filter(ImageFilter.GaussianBlur(0.8))
darkish = Image.fromarray(((L < 62) * 255).astype(np.uint8)).filter(ImageFilter.MinFilter(3)).filter(ImageFilter.GaussianBlur(1.2))
mask = Image.fromarray(np.minimum(np.asarray(wmask), np.asarray(darkish)).astype(np.uint8))
out = photo.copy(); out.paste(warped, (0, 0), mask)
sheen = Image.new('L', photo.size, 0)
ImageDraw.Draw(sheen).polygon([quad[0], quad[1], (quad[0][0] + (quad[3][0] - quad[0][0]) * 0.5, quad[0][1] + (quad[3][1] - quad[0][1]) * 0.5)], fill=26)
sheen = Image.fromarray(np.minimum(np.asarray(sheen), np.asarray(mask)).astype(np.uint8)).filter(ImageFilter.GaussianBlur(40))
out = Image.composite(Image.new('RGB', photo.size, (255, 255, 255)), out, sheen)
out.save(out_p, quality=92); print('saved', out.size, 'shot', shot.size)
