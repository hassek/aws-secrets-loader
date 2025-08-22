# Attack Reproduction: Supply Chain Attack via Package Name Confusion

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    SUPPLY CHAIN ATTACK REPRODUCTION                      │
│                         Package Name Confusion Attack                     │
└─────────────────────────────────────────────────────────────────────────┘

STEP 1: ATTACKER PREPARATION
┌──────────────────────────────────────────────────────────┐
│  🔴 ATTACKER                                              │
│  Creates malicious package: "aws-secrets-manager"        │
│  └─> Uploads to PUBLIC PyPI Repository                   │
│      └─> Same name as INTERNAL package                   │
│          └─> Contains malicious code                     │
└──────────────────────────────────────────────────────────┘
							⬇️

STEP 2: PIP INSTALLATION BEHAVIOR
┌──────────────────────────────────────────────────────────┐
│  📦 DEFAULT PIP SEARCH ORDER:                            │
│                                                           │
│  1️⃣ Internal Nexus Repository ──┐                        │
│                                  │                        │
│  2️⃣ Public PyPI Repository ─────┤                        │
│                                  │                        │
│  When version not found in       │                        │
│  Internal → Searches External    │                        │
└──────────────────────────────────────────────────────────┘
							⬇️

STEP 3: THE ATTACK EXECUTION
┌──────────────────────────────────────────────────────────┐
│  👨‍💻 DEVELOPER runs: pip install aws-secrets-manager     │
│                                                           │
│  ❌ Internal Nexus: Version not found or outdated        │
│  ✅ Public PyPI: Malicious package found!                │
│                                                           │
│  🚨 RESULT: Malicious package installed unknowingly      │
└──────────────────────────────────────────────────────────┘
							⬇️

STEP 4: ADDITIONAL ATTACK VECTOR
┌──────────────────────────────────────────────────────────┐
│  💻 LOCAL DEVELOPER MACHINE SCENARIO:                    │
│                                                           │
│  • Developer hasn't configured internal Nexus            │
│  • Runs: pip install aws-secrets-manager                 │
│  • Goes directly to Public PyPI                          │
│  • Even SAME VERSION can be malicious                    │
│                                                           │
│  🔓 COMPROMISED: Malicious code now has access          │
└──────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│                           ⚠️  KEY VULNERABILITIES                        │
├─────────────────────────────────────────────────────────────────────────┤
│ • Namespace confusion between internal and public repositories          │
│ • Default pip behavior prioritizes availability over security           │
│ • Developers may bypass internal repository unknowingly                 │
│ • Version matching doesn't guarantee package authenticity               │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│                           🛡️  PREVENTION MEASURES                        │
├─────────────────────────────────────────────────────────────────────────┤
│ • Configure pip to ONLY use internal repository                         │
│ • Use package pinning and hash verification                            │
│ • Implement namespace protection (unique internal prefixes)             │
│ • Regular security audits of dependencies                              │
│ • Use private package feeds with authentication                        │
└─────────────────────────────────────────────────────────────────────────┘
```
