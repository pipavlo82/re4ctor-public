# RE4CTOR Public Demo Stack

<div align="center">

## Verifiable Randomness Pipeline

**A reproducible measurement lab + methodology for cryptographic randomness on EVM (API surfaces, dual signatures, on-chain verification), with a small v0 dataset.**

**This is a demo stack, not a final production system.**

</div>

---

## What This Repository Contains

This repository demonstrates a complete end-to-end pipeline for verifiable random number generation:

**Pipeline Flow:**
1. **Core RNG API** – Cryptographic randomness source
2. **VRF/Dual-signature API** – ECDSA + ML-DSA-65 signed payloads
3. **Solidity Verifier** – `R4VRFVerifierCanonical` on-chain verification
4. **Lottery Contract** – `LotteryR4` demonstrates fair winner selection using verified randomness

**Purpose:** Provide a reproducible local testing environment for teams building applications that require cryptographically verifiable randomness.

---

## Verification Status

Recent full self-test results:

| Component | Status |
|-----------|--------|
| Health endpoints | ✅ PASS |
| Randomness generation | ✅ PASS |
| VRF dual payload retrieval | ✅ PASS |
| Hardhat contract tests | ✅ 6/6 passing |
| **Overall pipeline** | ✅ **7/7 checks passed** |

**Note:** Core API may return `429` responses under high concurrency (expected rate-limit behavior).

---

## Quick Start

### Prerequisites

- Docker & Docker Compose
- curl (for testing)
- Node.js & npm (for contract tests)

### 1. Start Services
```bash
docker compose -f docker-compose.public.yml up -d --build
```

### 2. Verify Health
```bash
# Core RNG API
curl -sS http://127.0.0.1:8089/health

# VRF Endpoint
curl -sS http://127.0.0.1:8082/health
```

### 3. Run Full Demo
```bash
bash scripts/run_full_demo.sh
```

**Expected output:**
```
DONE. All checks passed (7 OK).

Pipeline summary:
core RNG → signed randomness → Solidity verifier → Lottery fair winner
```

---

## Architecture
```
┌─────────────────┐
│   Core RNG API  │  Random number generation
└────────┬────────┘
         │
┌────────▼────────┐
│  VRF Gateway    │  ECDSA + ML-DSA-65 dual signing
└────────┬────────┘
         │
┌────────▼─────────────────┐
│  Solidity Contracts      │
│  • R4VRFVerifier         │  Signature verification
│  • LotteryR4             │  Fair winner selection
└──────────────────────────┘
```

---

## Table of Contents

- [Output Artifacts](#output-artifacts)
- [Smart Contracts](#smart-contracts)
- [Development](#development)
- [Use Cases](#use-cases)
- [Contributing](#contributing)
- [License](#license)

---

## Output Artifacts

Demo test run generates files in `/tmp`:

- `/tmp/r4_core_version.json` – Core API version info
- `/tmp/r4_core_rand_hex.txt` – Raw randomness sample
- `/tmp/r4_pq_health.json` – VRF health check
- `/tmp/vrf_dual.json` – Dual-signature payload
- `/tmp/vrf_verify_out.json` – Verification result

---

## Smart Contracts

### R4VRFVerifierCanonical

Verifies dual signatures (ECDSA + ML-DSA-65) on-chain.

### LotteryR4

Demonstrates fair winner selection using verified randomness.

**Example usage:**
```solidity
// Verify randomness
bool valid = verifier.verify(payload, signatures);

// Select winner
address winner = lottery.pickWinner(verifiedRandomness);
```

---

## Development

### Run Contract Tests
```bash
cd contracts
npm install
npx hardhat test
```

### Stop Services
```bash
docker compose -f docker-compose.public.yml down
```

---

## Use Cases

- 🎰 **Gaming & Lotteries** – Provably fair winner selection
- 🎲 **NFT Drops** – Unbiased trait generation and distribution
- 🔐 **Security Applications** – High-quality randomness with cryptographic proof
- 🧪 **Research & Education** – Learn verifiable randomness implementation patterns

---

## Contributing

Contributions welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Submit a pull request with clear description

---

## License

See [LICENSE](LICENSE) file for details.

---

## Support

- **Issues**: [GitHub Issues](../../issues)
- **Documentation**: See `/docs` directory
- **Examples**: Check `/examples` for integration samples

---

<div align="center">

**Built for transparency. Designed for trust.**

</div>
