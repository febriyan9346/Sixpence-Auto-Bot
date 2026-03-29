# Sixpence Auto Bot

🤖 Automated bot for Sixpence platform on Ethereum Sepolia Testnet

[![GitHub](https://img.shields.io/badge/GitHub-febriyan9346-blue?logo=github)](https://github.com/febriyan9346/Sixpence-Auto-Bot)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## 📌 Official Platform

🌐 **Sixpence Platform**: [https://www.sixpence.xyz/borrow](https://www.sixpence.xyz/borrow)

---

## 📖 Overview

Sixpence Auto Bot is an automated tool designed to interact with the Sixpence DeFi platform on Ethereum Sepolia Testnet. The bot performs various DeFi operations including:

- 💧 Claiming tokens from faucet
- 💰 Supplying assets to Aave lending protocol
- 🔄 Withdrawing assets from Aave
- 🏦 Depositing USDC to Vault
- 🔁 Swapping USDC to other tokens via Uniswap

## ✨ Features

- ✅ Multi-wallet support
- ✅ Proxy support for privacy
- ✅ Automated 24-hour cycle
- ✅ Support for multiple tokens (GOOGL, COIN, CRCL, TSLA, USDC, MSTR, NVDA, AVGO, MU, USDT, WETH)
- ✅ Colored console output with detailed logging
- ✅ Error handling and automatic retry
- ✅ Gas optimization

## 🔧 Prerequisites

- Python 3.8 or higher
- Ethereum Sepolia testnet ETH (for gas fees)
- Private keys of your wallets

## 📦 Installation

1. **Clone the repository**
```bash
git clone https://github.com/febriyan9346/Sixpence-Auto-Bot.git
cd Sixpence-Auto-Bot
```

2. **Install required dependencies**
```bash
pip install -r requirements.txt
```

3. **Configure your wallets**
   
   Create an `accounts.txt` file in the project directory and add your private keys (one per line):
   ```
   your_private_key_1
   your_private_key_2
   your_private_key_3
   ```

4. **(Optional) Configure proxies**
   
   If you want to use proxies, create a `proxy.txt` file with your proxies (one per line):
   ```
   http://user:pass@ip:port
   http://user:pass@ip:port
   ```

## 🚀 Usage

Run the bot:
```bash
python bot.py
```

The bot will ask you to choose:
- **Option 1**: Run with proxy
- **Option 2**: Run without proxy

The bot will then execute automated cycles every 24 hours.

## 📋 Supported Tokens

| Token | Symbol | Network |
|-------|--------|---------|
| Google | GOOGL | Sepolia |
| Coinbase | COIN | Sepolia |
| Circle | CRCL | Sepolia |
| Tesla | TSLA | Sepolia |
| USD Coin | USDC | Sepolia |
| MicroStrategy | MSTR | Sepolia |
| NVIDIA | NVDA | Sepolia |
| Broadcom | AVGO | Sepolia |
| Micron | MU | Sepolia |
| Tether | USDT | Sepolia |
| Wrapped Ether | WETH | Sepolia |

## ⚙️ Configuration

You can modify the following parameters in `bot.py`:

```python
self.claim_amt = 1000      # Amount to claim from faucet
self.supply_amt = 600      # Amount to supply to Aave
self.deposit_amt = 200     # Amount to deposit to Vault
self.swap_amt = 1          # Amount to swap per transaction
```

## 🔒 Security

- **Never share your private keys** with anyone
- Keep your `accounts.txt` file secure and never commit it to version control
- Use testnet only for testing purposes

## ⚠️ Disclaimer

This bot is for educational and testing purposes only. Use it at your own risk. The developers are not responsible for any loss of funds or other damages. Always test on testnet before using on mainnet.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/febriyan9346/Sixpence-Auto-Bot/issues).

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 💝 Support Us with Cryptocurrency

If you find this project helpful, you can support our development with cryptocurrency donations:

| Network | Wallet Address |
|---------|---------------|
| **EVM** (Ethereum, BSC, Polygon, etc.) | `0x216e9b3a5428543c31e659eb8fea3b4bf770bdfd` |
| **TON** (The Open Network) | `UQCEzXLDalfKKySAHuCtBZBARCYnMc0QsTYwN4qda3fE6tto` |
| **SOL** (Solana) | `9XgbPg8fndBquuYXkGpNYKHHhymdmVhmF6nMkPxhXTki` |
| **SUI** | `0x8c3632ddd46c984571bf28f784f7c7aeca3b8371f146c4024f01add025f993bf` |

Your support helps us continue developing and maintaining this project. Thank you! 🙏

---

## 📞 Contact

**Developer**: FEBRIYAN

**GitHub**: [@febriyan9346](https://github.com/febriyan9346)

---

<div align="center">
  
### ⭐ If you like this project, please give it a star! ⭐

Made with ❤️ by FEBRIYAN

</div>
