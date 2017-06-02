Step 1) run the python script
Step 2) done...

if it doesn't work....
make sure server address and port are updated
server_address = ('192.168.106.130', 6901)


------how it works-----------

Python client sends the below packet to the server, in the packet it has the x and y and room index for the 3rd level at the flags cordinates, 
it is already encoded with AES key "3DF2104AB016B2DE" which could have been found by runing the "strings" command to the game files on linux.
When the server decodes this data and sees that the "player" is on the flag of the 3rd level it will send a packet back saying to go to room 4 and will also
send the flag packet with the encoded MCA flag data which can be decoded with the same AES key. 

message = ('{ "command": "main", "x": ' 
		'"B8E65C3EB25022E2EFB6E4953BE25CBB",'
		' "y": "76834D38CD1B828B83A229D03198B38C",'
		' "room":"5C3350B0DB38B5EC1820C2EAADAD2D74' 	
		'"}')

