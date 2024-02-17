// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
contract ProposalContract {
    // Our contract code
    uint256 private counter;
    address owner;
    address[] private voted_addresses;
    struct Proposal {
        string title; // Title  of the proposal
        string description; // Description of the proposal
        uint256 approve; // Number of approve votes
        uint256 reject; // Number of reject votes
        uint256 pass; // Number of pass votes
        uint256 total_vote_to_end; // When the total votes in the proposal reaches this limit, proposal ends
        bool current_state; // This shows the current state of the proposal, meaning whether if passes of fails
        bool is_active; // This shows if others can vote to our contract
    }
    mapping(uint256 => Proposal) proposal_history; // Recordings of previous proposals
    constructor(){
        owner = msg.sender;
        voted_addresses.push(msg.sender);
    }
    modifier onlyOwner(){
        require(msg.sender == owner);
        _;
    }
    function create(string calldata _title, string calldata _description, uint256 _total_vote_to_end) external onlyOwner{
        counter += 1;
        proposal_history[counter] = Proposal(_title, _description, 0, 0, 0, _total_vote_to_end, false, true);
    }
    function setOwner(address _addr) public onlyOwner{
        owner = _addr;
    }
    function vote(uint8 choice) external {
        // Function logic
        Proposal storage proposal = proposal_history[counter];
        require(proposal.is_active == true, "The vote is not active.");
        require(!isVoted(msg.sender),"You have already done your vote.");
        uint256 total_vote = proposal.approve + proposal.reject + proposal.pass;
        voted_addresses.push(msg.sender);
        // Second part
        if (choice == 1) {
            proposal.approve += 1;
            proposal.current_state = calculateCurrentState();
        } else if (choice == 2) {
            proposal.reject += 1;
            proposal.current_state = calculateCurrentState();
        } else if (choice == 0) {
            proposal.pass += 1;
            proposal.current_state = calculateCurrentState();
        }

        // Third part
        if ((proposal.total_vote_to_end - total_vote == 1) && (choice == 1 || choice == 2 || choice == 0)) {
            proposal.is_active = false;
            voted_addresses = [owner];
        }
    }
    function isVoted(address _addr) private view returns(bool){
        for(uint i = 0; i < voted_addresses.length; i++){
            if(voted_addresses[i] == _addr){
                return true;
            }
        }
        return false;
    }
    function calculateCurrentState() private view returns(bool){
        Proposal storage proposal = proposal_history[counter];
        uint256 approve = proposal.approve;
        uint256 reject = proposal.reject;
        // uint256 pass = proposal.pass;

        // if(pass % 2 == 1){
        //     pass++;
        // }
        // pass = pass / 2;
        if(approve > reject ){
            return true;
        }
        else{
            return false;
        }
    }
    function terminateProposal() public onlyOwner{
        Proposal storage proposal = proposal_history[counter];
        require(proposal.is_active == true,"The vote is not active");
        proposal.is_active = false;
    }
    function getCurrentProposal() public view returns (Proposal memory){
        return proposal_history[counter];
    }
    function getProposal(uint256 num) public view returns(Proposal memory){
        return proposal_history[num];
    }
}