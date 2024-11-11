// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Bank{

    uint256 balance = 0;
    function withdraw() payable public {
        require(balance > 0 , "You dont have enough balance");
        payable(msg.sender).transfer(balance);
        balance =0;
    }
    
    function deposite() payable public {
        require(msg.value > 0 , "deposite amt should be greater than 0");
        balance += msg.value;
    }
    
    function showbalance() public view returns(uint){
        return  balance;
    }
}