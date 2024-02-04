# Introduction #
The main aim of the project is to eradicate the dependency of the storing the electronic health records on the central server and to make sharing of health records more secure...
- Now to store the data Ethereum block chain is used as it is robust and have the ability to execute the smart contracts
- The data is encrypted using the chaotic maping so as to ensure the privacy of the patient.
- The key to decrypt the data is only known by the patient and hence unauthorised access of can be mitigated.
- DICOM is the universal standard for storing the medical images in the electronic media. The size of these images is high. So these images are encrypted and uploaded onto the ipfs.
- IPFS is a decentralised file system and is a peer to peer network. Once the images are uploaded to the ipfs a hash is generated with which we can find the file in the ipfs.
- Once this is done, the patients demographic data, prescriptions, all the other medical conditions are taken as a text and to that text, this hash is added and encrypted using the chaotic mapping.
- To encrypt the text and images, the patient have to setup a key and the same key is used for the decryption
- This data is encoded using the Base-64 encoder. and uploaded to the blockchian.
- To shae the data, patient gives his id to the doctor he then retrives the encrypted data from the blockchain and then, the patient can enter the key to decrypt it. then the doctor can add or delete the
  data of the patient as necessary and upload to the blockchain once it is encrypted by the patient.

# Contents #
- The encoder folder contains the code for the Base-64 Encoder.
- The encryption folder contains the code for the text encryption.
- The images folder conatins the code for the image encryption.
- Smart contract is the solidity smart contract that interacts with the etherium block chain.

# Deployment #
- Clone the repository onto local machine.
- To deploy to code on the localhost navigate into each folder, then run the app.py file.
- The open browser and enter the http://localhost:5000
- You need to run one module at a time.
- The order in which you have to run the module is given in the implementation.

# Implementation #
Pleae refer the implementation.pdf for indetailed explenation of how to use the application
