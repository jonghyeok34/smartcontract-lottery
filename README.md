1. USser can enter lottery with ETH based on a USD fee
2. An admin will choose when the lottery is over
3. The lottery will select a random winner

How do we want to test this?

1. `mainnet-fork`
2. `development with mocks`
3. `test net`

- brownie add mainnet-for
```
brownie networks add development mainnet-fork cmd=ganache-cli host=http://127.0.0.1 fork=<ALCHEMY http key> accounts=10 mnemonic=brownie port=8545
```
- install 
```
brownie pm install OpenZeppelin/openzeppelin-contracts@v3.4.0
```

- pseudo random numbers
```
Random number should not used because of security - it can be exploited
```
- chainlink verifiable randomness