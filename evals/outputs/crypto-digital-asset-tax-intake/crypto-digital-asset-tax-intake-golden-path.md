# Crypto / Digital Asset Tax Intake — Whitfield Consulting LLC, Tax Year [CONFIRM: tax year]

> **Draft for attorney/tax-professional review. Not legal advice or tax advice.** This is draft work product organizing digital-asset records for a qualified tax professional. It does not calculate gain or loss, determine tax treatment, or prepare any filing-ready schedule.

## 1. Gates Table

| Gate | Value | Source |
|---|---|---|
| Taxpayer / entity type | Single-member LLC, disregarded entity as stated by user `[CONFIRM: entity classification]` | User-stated |
| Jurisdiction(s) | United States (federal); state `[CONFIRM: state tax jurisdiction]` | User-stated |
| Tax year / period | As stated by user `[deadline verification required]` | User-stated |
| User's role | In-house counsel preparing intake package for outside tax professional | User-stated |
| Accounts | Wallet `[MASKED: wallet-1]`; exchange account `[MASKED: exchange-1]` | User-stated, masked per default |

## 2. Crypto / Digital Asset Tax Intake Matrix

| Activity category | Business vs personal | Records provided | Record completeness | Source | Missing records | Open question for tax professional |
|---|---|---|---|---|---|---|
| Purchases | Business, as characterized by user | Exchange trade history export | Complete | `exchange-export-1099b.csv` | None identified | Confirm cost-basis method applied by the exchange `[CONFIRM]` |
| Swaps / trades | Business, as characterized by user | Wallet transaction log | Partial | `wallet-1-tx-log.csv` | Gas-fee records for several rows | Does fee treatment differ by transaction type? `[CONFIRM]` |
| Staking rewards | Ambiguous — not characterized by user | Exchange staking-rewards report | Complete | `exchange-staking-report.pdf` | None identified | What is the recognition-timing question the professional should evaluate? `[CONFIRM]` |
| NFT sale | Business, as characterized by user | Marketplace transaction receipt | Complete | `nft-marketplace-receipt.pdf` | Original acquisition record for the NFT | Is the acquisition record needed before further evaluation is possible? `[CONFIRM]` |
| Airdrops | Ambiguous | Wallet transaction log | Partial | `wallet-1-tx-log.csv` | Fair-market-value data at receipt | What valuation source should the professional use? `[CONFIRM]` |

## 3. Missing Records List

- Fair-market-value data at the time of each airdrop receipt.
- Gas-fee detail for a subset of the swap/trade rows in the wallet log.
- The original acquisition record for the NFT later sold.

## 4. Document Request List

- Complete Form 1099 series documents, if issued by any exchange, with citations to the specific box and line.
- Any prior-year basis carryover schedule, if this is not the taxpayer's first reporting year.
- State-level digital-asset guidance the taxpayer has already received, if any `[CONFIRM]`.

## 5. Uncertainty Flags

- Whether staking rewards and airdrops should be characterized as business or personal activity is not resolved here `[CONFIRM]`.
- Entity classification (disregarded entity vs. other) has not been independently verified against filed elections `[CONFIRM: entity classification]`.
- State tax jurisdiction beyond the federal filing has not been confirmed `[CONFIRM: state tax jurisdiction]`.

## 6. Tax-Professional Verification Questions

- Given the partial wallet records, is additional data collection needed before any gain/loss analysis can begin?
- Does the NFT sale require the missing acquisition record before the professional can evaluate it?
- What valuation methodology should apply to the airdrop and staking-reward receipts, and does that vary by jurisdiction? `[CONFIRM]`

## 7. Assumptions and Unresolved Items

- Assumed the wallet and exchange exports as provided are complete for the categories marked "Complete" above; not independently verified.
- Assumed the entity is a disregarded entity as the user described; not verified against a filed election.
- No gain or loss, basis, or holding-period calculation is made anywhere in this intake. No tax treatment is determined. These are reserved for the qualified tax professional.

## Attorney Verification Checklist

- [ ] Taxpayer/entity type, jurisdictions, tax period, and role are confirmed.
- [ ] Every row in the intake matrix cites its source record.
- [ ] No gain/loss, basis, or holding-period calculation appears above.
- [ ] No Form 8949 or filing-ready schedule appears above.
- [ ] No foreign-account reporting conclusion appears above.
- [ ] Wallet addresses and account numbers remain masked.
- [ ] No invented digital-asset tax rules, rates, forms, or citations appear.
- [ ] A qualified tax professional has reviewed this intake before any return preparation or tax-authority communication.
