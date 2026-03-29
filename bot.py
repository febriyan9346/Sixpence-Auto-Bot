import os
import time
import random
from datetime import datetime
import pytz
from colorama import Fore, Style, init
from web3 import Web3
import warnings
import sys

os.system('clear' if os.name == 'posix' else 'cls')
warnings.filterwarnings('ignore')
if not sys.warnoptions:
    os.environ["PYTHONWARNINGS"] = "ignore"
init(autoreset=True)

class SixpenceBot:
    def __init__(self):
        self.rpc_url = "https://eth-sepolia.g.alchemy.com/v2/UNS1jOCemmN16O67Ypw7ftDgu6Yqwp5O"
        self.faucet_contract = "0xcf59F40fCD6066dFf084AcceEEe51A98641626b1"
        self.pool_contract = "0x62ee6Aaf2aFaC4f0a3213e9F929Fc054F6C6befA"
        self.router_contract = "0xeE567Fe1712Faf6149d80dA1E6934E354124CfE3"
        self.vault_contract = "0x811027e0B0c4fFD8053b9c16005Fb390f57a1058"
        self.usdc_address = "0x53aeb957be8f9ca48327c2344a8cc12257213d5d"
        self.usdc_decimals = 6
        self.claim_amt = 1000
        self.supply_amt = 600
        self.deposit_amt = 200
        self.swap_amt = 1
        self.tokens = [
            {"symbol": "GOOGL", "address": "0x05f5632dea903e85189c60c5be8a140c05c018fe", "decimals": 18},
            {"symbol": "COIN",  "address": "0x37fe0c16d8db827a8f70ef5c5e1795f1d2871522", "decimals": 18},
            {"symbol": "CRCL",  "address": "0x41cac4419c72f02e754eb34e2c28ceeda7e66558", "decimals": 18},
            {"symbol": "TSLA",  "address": "0x452eaa5f0a9ab7a92bf3e82bd7bbee3cbf5e0b28", "decimals": 18},
            {"symbol": "USDC",  "address": "0x53aeb957be8f9ca48327c2344a8cc12257213d5d", "decimals": 6},
            {"symbol": "MSTR",  "address": "0x593b8fec0c0b451a110f81e3e52a37022ce5d4c3", "decimals": 18},
            {"symbol": "NVDA",  "address": "0x5f0218af2268fc8aceb1e6d707c501975e4f7af3", "decimals": 18},
            {"symbol": "AVGO",  "address": "0x6095548b9bcb5b9862738c960d2d7cc0c5731695", "decimals": 18},
            {"symbol": "MU",    "address": "0x8abb0dd8a0d651ba0404d68593326a0fb6288a88", "decimals": 18},
            {"symbol": "USDT",  "address": "0xa2f47b34de37aeaca14488cb28dbf8cb6efab869", "decimals": 6},
            {"symbol": "WETH",  "address": "0xfff9976782d46cc05630d1f6ebab18b2324d6b14", "decimals": 18}
        ]
        self.erc20_abi = [
            {"constant": True, "inputs": [{"name": "_owner", "type": "address"}], "name": "balanceOf", "outputs": [{"name": "balance", "type": "uint256"}], "type": "function"},
            {"constant": True, "inputs": [{"name": "owner", "type": "address"}, {"name": "spender", "type": "address"}], "name": "allowance", "outputs": [{"name": "", "type": "uint256"}], "type": "function"},
            {"constant": False, "inputs": [{"name": "spender", "type": "address"}, {"name": "amount", "type": "uint256"}], "name": "approve", "outputs": [{"name": "", "type": "bool"}], "type": "function"}
        ]
        self.router_abi = [{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactTokensForTokens","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"nonpayable","type":"function"}]
        self.pool_abi = [
            {"inputs":[{"internalType":"address","name":"asset","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"address","name":"onBehalfOf","type":"address"},{"internalType":"uint16","name":"referralCode","type":"uint16"}],"name":"supply","outputs":[],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[{"internalType":"address","name":"asset","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"address","name":"to","type":"address"}],"name":"withdraw","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"nonpayable","type":"function"}
        ]
        self.vault_abi = [{"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"depositToken","outputs":[],"stateMutability":"nonpayable","type":"function"}]

    def get_wib_time(self):
        wib = pytz.timezone('Asia/Jakarta')
        return datetime.now(wib).strftime('%H:%M:%S')
    
    def print_banner(self):
        banner = f"""
{Fore.CYAN}SIXPENCE AUTO BOT{Style.RESET_ALL}
{Fore.WHITE}By: FEBRIYAN{Style.RESET_ALL}
{Fore.CYAN}============================================================{Style.RESET_ALL}
"""
        print(banner)

    def log(self, message, level="INFO"):
        time_str = self.get_wib_time()
        if level == "INFO":
            color = Fore.CYAN
            symbol = "[INFO]"
        elif level == "SUCCESS":
            color = Fore.GREEN
            symbol = "[SUCCESS]"
        elif level == "ERROR":
            color = Fore.RED
            symbol = "[ERROR]"
        elif level == "WARNING":
            color = Fore.YELLOW
            symbol = "[WARNING]"
        elif level == "CYCLE":
            color = Fore.MAGENTA
            symbol = "[CYCLE]"
        else:
            color = Fore.WHITE
            symbol = "[LOG]"
        print(f"[{time_str}] {color}{symbol} {message}{Style.RESET_ALL}")

    def random_delay(self):
        delay = random.randint(1, 3)
        time.sleep(delay)

    def show_menu(self):
        print(f"{Fore.CYAN}============================================================{Style.RESET_ALL}")
        print(f"{Fore.CYAN}Select Mode:{Style.RESET_ALL}")
        print(f"{Fore.GREEN}1. Run with proxy")
        print(f"2. Run without proxy{Style.RESET_ALL}")
        print(f"{Fore.CYAN}============================================================{Style.RESET_ALL}")
        while True:
            try:
                choice = input(f"{Fore.GREEN}Enter your choice (1/2): {Style.RESET_ALL}").strip()
                if choice in ['1', '2']:
                    return choice
                else:
                    print(f"{Fore.RED}Invalid choice! Please enter 1 or 2.{Style.RESET_ALL}")
            except KeyboardInterrupt:
                print(f"\n{Fore.RED}Program terminated by user.{Style.RESET_ALL}")
                exit(0)

    def countdown(self, seconds):
        for i in range(seconds, 0, -1):
            hours = i // 3600
            minutes = (i % 3600) // 60
            secs = i % 60
            print(f"\r[COUNTDOWN] Next cycle in: {hours:02d}:{minutes:02d}:{secs:02d} ", end="", flush=True)
            time.sleep(1)
        print("\r" + " " * 60 + "\r", end="", flush=True)

    def get_w3(self, proxy=None):
        try:
            if proxy:
                req_kwargs = {"proxies": {"http": proxy, "https": proxy}}
                return Web3(Web3.HTTPProvider(self.rpc_url, request_kwargs=req_kwargs))
            return Web3(Web3.HTTPProvider(self.rpc_url))
        except Exception as e:
            self.log(f"Failed to initialize Web3: {e}", "ERROR")
            return None

    def send_transaction(self, w3, private_key, wallet_address, to_address, input_data, tx_name):
        try:
            tx = {'to': to_address, 'value': 0, 'chainId': 11155111, 'data': input_data, 'from': wallet_address}
            gas_estimate = w3.eth.estimate_gas(tx)
            tx['gas'] = int(gas_estimate * 1.2)
            tx['nonce'] = w3.eth.get_transaction_count(wallet_address, 'pending')
            tx['maxFeePerGas'] = int(w3.eth.gas_price * 1.5)
            tx['maxPriorityFeePerGas'] = w3.eth.max_priority_fee
            del tx['from']
            signed_tx = w3.eth.account.sign_transaction(tx, private_key)
            tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
            self.log(f"{tx_name} Sent! Hash: {w3.to_hex(tx_hash)}", "INFO")
            receipt = w3.eth.wait_for_transaction_receipt(tx_hash, timeout=120)
            if receipt.status == 1:
                self.log(f"{tx_name} SUKSES!", "SUCCESS")
                return True
            else:
                self.log(f"{tx_name} GAGAL (Reverted)!", "ERROR")
                return False
        except Exception as e:
            self.log(f"Error {tx_name}: {str(e)}", "WARNING")
            return False

    def ensure_approval(self, w3, private_key, wallet_address, token_contract, token_symbol, spender_address, amount_needed, spender_name):
        try:
            allowance = token_contract.functions.allowance(wallet_address, spender_address).call()
            if allowance < amount_needed:
                self.log(f"Approve {token_symbol} for {spender_name}...", "INFO")
                approve_data = token_contract.encodeABI(fn_name="approve", args=[spender_address, 2**256 - 1])
                self.send_transaction(w3, private_key, wallet_address, token_contract.address, approve_data, f"Approve {token_symbol}")
            else:
                self.log(f"Allowance {token_symbol} already OK.", "SUCCESS")
        except Exception as e:
            self.log(f"Failed to check/approve allowance for {token_symbol}: {e}", "WARNING")

    def run(self):
        self.print_banner()
        if not os.path.exists("accounts.txt"):
            self.log("File 'accounts.txt' not found!", "ERROR")
            return
        with open("accounts.txt", "r") as file:
            keys = [k.strip() for k in file.read().splitlines() if k.strip()]
        if not keys:
            self.log("File 'accounts.txt' is empty!", "ERROR")
            return

        proxies = []
        choice = self.show_menu()
        if choice == '1':
            if not os.path.exists("proxy.txt"):
                self.log("File 'proxy.txt' not found!", "ERROR")
                return
            with open("proxy.txt", "r") as file:
                proxies = [p.strip() for p in file.read().splitlines() if p.strip()]
            if not proxies:
                self.log("File 'proxy.txt' is empty!", "ERROR")
                return
            self.log("Running with proxy", "INFO")
        else:
            self.log("Running without proxy", "INFO")

        self.log(f"Loaded {len(keys)} accounts successfully", "INFO")
        print(f"\n{Fore.CYAN}============================================================{Style.RESET_ALL}\n")

        cycle = 1
        while True:
            self.log(f"Cycle #{cycle} Started", "CYCLE")
            print(f"{Fore.CYAN}------------------------------------------------------------{Style.RESET_ALL}")
            
            success_count = 0
            for i, pk in enumerate(keys):
                try:
                    proxy = proxies[i % len(proxies)] if proxies else None
                    w3 = self.get_w3(proxy)
                    if not w3 or not w3.is_connected():
                        self.log("RPC Connection Failed! Skipping account.", "ERROR")
                        continue
                    
                    wallet_address = w3.eth.account.from_key(pk).address
                    mask_addr = f"{wallet_address[:6]}...{wallet_address[-4:]}"
                    
                    self.log(f"Account #{i+1}/{len(keys)}", "INFO")
                    self.log(f"Proxy: {proxy if proxy else 'No Proxy'}", "INFO")
                    self.log(f"Address: {mask_addr}", "INFO")

                    if w3.eth.get_balance(wallet_address) == 0:
                        self.log("Sepolia ETH balance is 0! Skipping.", "ERROR")
                        continue
                    
                    self.log("Login successful!", "SUCCESS")
                    self.random_delay()

                    contracts = {}
                    for t in self.tokens:
                        contracts[t["symbol"]] = w3.eth.contract(address=w3.to_checksum_address(t["address"]), abi=self.erc20_abi)
                    
                    usdc_contract = contracts["USDC"]
                    pool_contract = w3.eth.contract(address=w3.to_checksum_address(self.pool_contract), abi=self.pool_abi)
                    router_contract = w3.eth.contract(address=w3.to_checksum_address(self.router_contract), abi=self.router_abi)
                    vault_contract = w3.eth.contract(address=w3.to_checksum_address(self.vault_contract), abi=self.vault_abi)

                    self.log("Phase 1: Claim Faucet", "INFO")
                    for t in self.tokens:
                        try:
                            amt_claim = int(self.claim_amt * (10 ** t["decimals"]))
                            p_token = t["address"].lower().replace("0x", "").zfill(64)
                            p_recv = wallet_address.lower().replace("0x", "").zfill(64)
                            p_amt = hex(amt_claim).replace("0x", "").zfill(64)
                            c_data = f"0xc6c3bbe6{p_token}{p_recv}{p_amt}"
                            self.send_transaction(w3, pk, wallet_address, w3.to_checksum_address(self.faucet_contract), c_data, f"Claim {t['symbol']}")
                        except Exception as e:
                            self.log(f"Phase 1 error for {t['symbol']}: {e}", "WARNING")

                    self.log("Phase 2: Supply to Aave", "INFO")
                    for t in self.tokens:
                        try:
                            bal_wei = contracts[t["symbol"]].functions.balanceOf(wallet_address).call()
                            amt_sup = int(self.supply_amt * (10 ** t["decimals"]))
                            act_sup = amt_sup if bal_wei >= amt_sup else bal_wei

                            if t["symbol"] == "USDC":
                                res_swap = int(self.swap_amt * (10 ** self.usdc_decimals)) * (len(self.tokens) - 1)
                                if bal_wei > res_swap:
                                    act_sup = bal_wei - res_swap
                                else:
                                    act_sup = 0

                            if act_sup > 0:
                                self.ensure_approval(w3, pk, wallet_address, contracts[t["symbol"]], t["symbol"], w3.to_checksum_address(self.pool_contract), act_sup, "Aave")
                                s_data = pool_contract.encodeABI(fn_name="supply", args=[w3.to_checksum_address(t["address"]), act_sup, wallet_address, 0])
                                self.send_transaction(w3, pk, wallet_address, w3.to_checksum_address(self.pool_contract), s_data, f"Supply {t['symbol']}")
                        except Exception as e:
                            self.log(f"Phase 2 error for {t['symbol']}: {e}", "WARNING")

                    self.log("Phase 3: Withdraw from Aave", "INFO")
                    for t in self.tokens:
                        try:
                            w_data = pool_contract.encodeABI(fn_name="withdraw", args=[w3.to_checksum_address(t["address"]), 2**256 - 1, wallet_address])
                            self.send_transaction(w3, pk, wallet_address, w3.to_checksum_address(self.pool_contract), w_data, f"Withdraw {t['symbol']}")
                        except Exception as e:
                            self.log(f"Phase 3 error for {t['symbol']}: {e}", "WARNING")

                    self.log("Phase 4: Deposit USDC to Vault", "INFO")
                    try:
                        usdc_bal = usdc_contract.functions.balanceOf(wallet_address).call()
                        dep_wei = int(self.deposit_amt * (10 ** self.usdc_decimals))
                        if usdc_bal >= dep_wei:
                            self.ensure_approval(w3, pk, wallet_address, usdc_contract, "USDC", w3.to_checksum_address(self.vault_contract), dep_wei, "Vault")
                            d_data = vault_contract.encodeABI(fn_name="depositToken", args=[dep_wei])
                            self.send_transaction(w3, pk, wallet_address, w3.to_checksum_address(self.vault_contract), d_data, "Deposit USDC")
                        else:
                            self.log("Not enough USDC to deposit", "WARNING")
                    except Exception as e:
                        self.log(f"Phase 4 error: {e}", "WARNING")

                    self.log("Phase 5: Swap USDC to Others", "INFO")
                    try:
                        u_bal = usdc_contract.functions.balanceOf(wallet_address).call()
                        s_wei = int(self.swap_amt * (10 ** self.usdc_decimals))
                        
                        if u_bal >= s_wei:
                            self.ensure_approval(w3, pk, wallet_address, usdc_contract, "USDC", w3.to_checksum_address(self.router_contract), s_wei * len(self.tokens), "Uniswap")
                            for t in self.tokens:
                                try:
                                    if t["symbol"] == "USDC": continue
                                    if usdc_contract.functions.balanceOf(wallet_address).call() < s_wei: break
                                    
                                    path = [w3.to_checksum_address(self.usdc_address), w3.to_checksum_address(t["address"])]
                                    dl = int(time.time()) + 600
                                    sw_data = router_contract.encodeABI(fn_name="swapExactTokensForTokens", args=[s_wei, 0, path, wallet_address, dl])
                                    self.send_transaction(w3, pk, wallet_address, w3.to_checksum_address(self.router_contract), sw_data, f"Swap USDC -> {t['symbol']}")
                                except Exception as e:
                                    self.log(f"Swap error for {t['symbol']}: {e}", "WARNING")
                        else:
                            self.log("Not enough USDC for swap", "WARNING")
                    except Exception as e:
                        self.log(f"Phase 5 error: {e}", "WARNING")
                    
                    self.log("Task Completed for this account", "SUCCESS")
                    success_count += 1
                    
                except Exception as e:
                    self.log(f"Critical error processing account {i+1}: {e}", "ERROR")

                if i < len(keys) - 1:
                    print(f"{Fore.WHITE}............................................................{Style.RESET_ALL}")
                    time.sleep(2)

            print(f"{Fore.CYAN}------------------------------------------------------------{Style.RESET_ALL}")
            self.log(f"Cycle #{cycle} Complete | Success: {success_count}/{len(keys)}", "CYCLE")
            print(f"{Fore.CYAN}============================================================{Style.RESET_ALL}\n")
            
            cycle += 1
            self.countdown(86400)

if __name__ == "__main__":
    bot = SixpenceBot()
    bot.run()
