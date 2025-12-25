// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.8.20;

contract RM_Xmas_List3 {
    address public santaClaus;

    struct Elf {
        string name;
        uint256 level;
        address account;
    }

    struct Gift {
        string description;
        uint256 elfId; 
        uint256 childId;
        address childFor;
        bool delivered;
    }

    struct Child {
        string name;
        address reservedFor;
        bool delivered;
    }

    Elf[] public elves;
    Gift[] public gifts;
    Child[] public children;

    mapping(address => uint256) public elvesId;
    mapping(address => uint256) public childId;
    mapping(address => uint256) public childNonce;

    bytes32 private magicXmasS3cr3t; 

    modifier onlySanta() {
        require(msg.sender == santaClaus, "Only Santa can access this function");
        _;
    }

    modifier onlyElf() {
        require(elvesId[msg.sender] > 0, "Only Elf");
        _;
    }

    constructor(bytes32 _magicXmasS3cr3t) {
        santaClaus = msg.sender;
        magicXmasS3cr3t = keccak256(abi.encodePacked(_magicXmasS3cr3t, santaClaus));
    }

    function registerElf(string calldata _name, uint256 _level, address _account) external onlySanta returns (uint256 id) {
        require(_account != address(0), "zero address");
        require(elvesId[_account] == 0, "already elf");

        id = elves.length;
        elves.push(Elf({name: _name, level: _level, account: _account}));
        elvesId[_account] = id + 1;
    }

    function registerChild(string calldata _name) external returns (uint256 id) {
        require(childId[msg.sender] == 0, "already registered");
        id = children.length;
        children.push(Child({name: _name, reservedFor: msg.sender, delivered: false}));
        childId[msg.sender] = id + 1;
    }

    function prepareGift(string calldata _description, uint256 _childId) external onlyElf returns (uint256 giftId) {
        require(_childId < children.length, "Invalid child");

        Gift memory gift = Gift({
            description: _description,
            elfId: elvesId[msg.sender],
            childId: _childId,
            childFor: children[_childId].reservedFor,
            delivered: false
        });

        giftId = gifts.length;
        gifts.push(gift);
    }

    function deliverGift(uint256 _giftId) external onlyElf {
        require(_giftId < gifts.length, "Invalid gift");
        Gift storage g = gifts[_giftId];
        require(!g.delivered, "Already delivered");
        g.delivered = true;
        children[g.childId].delivered = true;
    }

    function getElvesCount() external view returns (uint256) {
        return elves.length;
    }

    function claimElfBySecret(string calldata _name, bytes32 _guess) external {
        require(_guess == magicXmasS3cr3t, "Bad magic Xmas Secret Word");
        uint256 id = elves.length;
        elves.push(Elf({name: _name, level: 1, account: msg.sender}));
        elvesId[msg.sender] = id + 1;
    }
    
    function getGiftInfo(uint256 _giftId) external view returns (
            string memory description,
            uint256 elfId,
            string memory childName,
            address childFor,
            bool delivered
        )
    {
        require(_giftId < gifts.length, "Invalid gift");
        Gift storage g = gifts[_giftId];
        description = g.description;
        elfId = g.elfId;
        childName = children[g.childId].name;
        childFor = g.childFor;
        delivered = g.delivered;
    }
    
    function getChildInfo(uint256 _id) external view returns (
            string memory name,
            address reservedFor,
            bool delivered
        )
    {
        require(_id < children.length, "Invalid Child ID");
        Child storage c = children[_id];
        name = c.name;
        reservedFor = c.reservedFor;
        delivered = c.delivered;
    }

    function getElfInfo(uint256 _id) external view returns (
            string memory name,
            uint256 level,
            address account
        )
    {
        require(_id < elves.length, "Invalid elf ID");
        Elf storage a = elves[_id];
        name = a.name;
        level = a.level;
        account = a.account;
    }

    function isSolved() external view returns (bool) {
        return elvesId[msg.sender] > 0;
    }
}

