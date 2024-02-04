// SPDX-License-Identifier: MIT

pragma solidity ^0.8.7;


contract PatientData {
    uint256 favoriteNumber;

    struct Patients {
        string uid;
        string info;
    }

    Patients[] public patients;

    mapping(string => string) public uidToData;


    function addPatient(
        string memory _uid,
        string memory _information
    ) public {
        patients.push(Patients(_uid, _information));
        uidToData[_uid] = _information;
    }
    

}
