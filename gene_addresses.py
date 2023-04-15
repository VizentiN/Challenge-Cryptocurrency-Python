from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
import ecdsa
import hashlib
import base58
from web3 import Web3, Account


def generate_btc_address():
    # Generate a new private key
    private_key = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)

    # Calculate the corresponding public key
    public_key = private_key.get_verifying_key().to_string()

    # Calculate the address from the public key
    sha256_hash = hashlib.sha256(public_key).digest()
    ripemd160_hash = hashlib.new('ripemd160', sha256_hash).digest()
    address_bytes = b'\x00' + ripemd160_hash
    chksum_full = hashlib.sha256(
        hashlib.sha256(address_bytes).digest()).digest()
    address = base58.b58encode(address_bytes + chksum_full[:4]).decode('utf-8')

    # Output the address and private key as strings
    return (address, private_key.to_string().hex())


def generate_eth_address():
    # Connect to a local Ethereum node (replace with your own endpoint if needed)
    web3 = Web3(Web3.HTTPProvider('http://localhost:8545'))

    # Generate a new Ethereum account and get the address and private key
    account = Account.create()
    eth_address = account.address
    eth_private_key = account._private_key.hex()

    # Output the address and private key
    return (eth_address, eth_private_key)


def generate_ltc_address():
    # Generate a new RSA keypair
    key = RSA.generate(2048)

    # Calculate the Litecoin address from the public key
    pubkey = key.publickey().export_key(format='DER')
    sha256 = SHA256.new(pubkey)
    pubkey_hash = SHA256.new(sha256.digest()).digest()
    address = 'L' + pubkey_hash[-20:].hex()

    # Output the address and private key as strings
    return (address, key.export_key(format='PEM'))


def generate_doge_address():
    # Generate a new private key
    private_key = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)

    # Get the corresponding public key
    public_key = private_key.verifying_key.to_string()

    # Compute the public key hash (RIPEMD-160 hash of SHA-256 hash of public key)
    sha256_hash = hashlib.sha256(public_key).digest()
    ripe_hash = hashlib.new('ripemd160', sha256_hash).digest()

    # Add version byte to the front (30 for Dogecoin)
    version_ripe_hash = b'\x1e' + ripe_hash

    # Compute the checksum (first four bytes of SHA-256 of SHA-256 of version + hash)
    first_sha256 = hashlib.sha256(version_ripe_hash).digest()
    second_sha256 = hashlib.sha256(first_sha256).digest()
    checksum = second_sha256[:4]

    # Append the checksum to the version + hash
    binary_address = version_ripe_hash + checksum

    # Convert the binary address to base58 for readability
    base58_address = base58.b58encode(binary_address)
    address = base58_address.decode()
    private_key = private_key.to_string().hex()

    return (address, private_key)
