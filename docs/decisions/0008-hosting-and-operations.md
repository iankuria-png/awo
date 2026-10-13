# ADR 0008: Hosting and operations on Vultr in Johannesburg

- **Status:** Proposed (foundation pass, T-120, 13 October 2026). Not in the decision log until Ian decides. Hosting itself is decided (D-043).
- **Relates to:** D-002, D-016, D-043; Q-17, Q-47, Q-50; T-119; doc 04 (Hosting); doc 17 §8.

## Context

Production runs on Vultr in Johannesburg, Vultr's only South African region, which has no object storage (D-043). One person operates everything, so the setup must be boring, documented and restorable. Every external service needs a data-location note. Facts below were checked on 13 October 2026 (doc 17, Appendix F).

## Proposed decision

```
             ┌──────────────── Vultr, Johannesburg ─────────────────┐
 members ──► │ Caddy 2.11 (TLS) ─► web (Next.js)   api ─► Postgres 18 │
             │                       │              │      ▲          │
             │                    workers (pg-boss) ─┘      │ pgBackRest│
             │ GlitchTip · Umami · Gatus      files (block storage)   │
             └──────────────────────────────────────────┼───────────┘
                                                         ▼ encrypted
                                          AWS S3, af-south-1 (Cape Town)
```

| Concern | Proposal | Licence or price | Data-location note |
|---|---|---|---|
| Servers | One Vultr VPS for production; staging on the same server at first (its own database), its own small VPS later | Vultr pricing (Ian's account) | Johannesburg |
| Deploy | Docker Compose and Caddy 2.11; GitHub Actions builds images and deploys over SSH; Kamal 2 if zero-downtime swaps become worth it | Free (Apache-2.0, MIT) | Images on GitHub's registry (US) hold code only, never data |
| Database | PostgreSQL 18, self-managed in a container with a block-storage volume | Free | Johannesburg |
| Files | Block storage on the server, behind the API (no public bucket); SeaweedFS (Apache-2.0) only if an S3 API is ever needed. Not MinIO (archived) | Free | Johannesburg |
| Backups | **pgBackRest 2.59**: repo 1 on the server (fast restores), repo 2 **encrypted in AWS S3 af-south-1, Cape Town** (Standard-IA, versioning or Object Lock); restic for files to the same bucket. Vultr's automatic backups for quick rollbacks; never snapshots of servers with member data (snapshots span regions) | pgBackRest and restic free; S3 about $0.015 a GB-month (about $1 a month for 50 GB). **Paid: Ian's call** | Cape Town, a second South African city (answers Q-50 if Ian agrees) |
| Restore drills | Nightly `pgbackrest check` and `verify` with an alert; monthly, an automated restore to a throwaway VPS with smoke checks, recording time and data lost; quarterly, a full rehearsal by a person | Pennies a month | Johannesburg and Cape Town |
| Errors | **GlitchTip 6** (Sentry-compatible SDKs, runs on Postgres, about 512 MB) | Free (MIT) | Johannesburg |
| Uptime | **Gatus** or Uptime Kuma on the server, plus one free external check from outside South Africa so a dead server still raises an alert | Free | The external check sees only the public URL |
| Logs and metrics | Docker logs with rotation at first; Grafana, Loki and Alloy when needed; OpenTelemetry in the code so the back end can change | Free | Johannesburg |
| Analytics | **Umami 3** on the same Postgres; no member identifiers in events | Free (MIT) | Johannesburg |
| Email (Q-17, Q-47) | **Amazon SES in af-south-1 (Cape Town)**, through its API (no SMTP endpoint there); content follows Q-47's proposal (no amounts, score or stage) | $0.10 per 1 000 emails. **Paid: Ian's call** | Cape Town: the only provider checked that processes in South Africa |
| Push | Web Push with VAPID from our own server, with content-free payloads ("You have a check-in"); FCM and APNs directly for native apps later | Free | Payloads encrypted end to end; the browser's push service sees only metadata |
| Sign-in codes | Behind AWO's own sender interface; the provider (SMS or WhatsApp) waits on a data-location decision (ADR 0007) | Paid: Ian's call | Every provider checked processes outside South Africa |
| Secrets | On the server in files only the service can read; CI secrets in GitHub Actions; a Vultr API key for Claude as a network secret on the cloud environment, never in the repo | — | — |

**Runbooks** (`docs/operations/`): deploy and roll back, back up and restore, rotate a secret, an incident, renew domains.

## Alternatives

- **A self-hosted platform** (Coolify, Dokploy): a web UI, but another control plane on the same small server.
- **Sentry self-hosted:** needs at least 16 GB of RAM; too heavy.
- **Plausible or PostHog:** need ClickHouse; more than AWO needs.
- **A second Johannesburg provider for backups** (Google, Oracle, Huawei): in South Africa, but the same city as Vultr, which weakens the point of a second location.
- **Azure South Africa West (Cape Town):** access by request only.

## Consequences

- Two paid services beyond Vultr, both cents to a few dollars a month: S3 in Cape Town and SES in Cape Town. Both AWS, in South Africa.
- Everything else is free, self-hosted and inside South Africa.

## Ian decides

AWS in Cape Town for backups (Q-50) and email (Q-17); the uptime check from outside South Africa (it sees only the public URL); and when staging gets its own server.
