import parkingApp
import pytest

#@pytest.mark.skip(reason="This test fails")
def test_status():
	jmustatus1 = parkingApp.status("Resident")
	assert (jmustatus1 == ["R1","R2","R3","R4","R5","R6","R7","R8","R9","R10","R11","R12","R13","R14"])

	jmustatus2 = parkingApp.status("Commuter")
	assert (jmustatus2 == ["C1 Lot", "C2 Lot", "C3 Lot", "C4 Lot", "C6 Lot", "C7 Lot", "C8 Lot", "C9 Lot", "C10 Lot", "C11 Lot", "C12 Lot", "C13 Lot", "C14 Lot", "C15 Lot", "C16 Lot", "C17 Lot", "C18 Lot", "C19 Lot", "Champions Drive Deck Level 2", "Champions Drive Deck Level 3", "Champions Drive Deck Level 4", "Champions Drive Deck Level 5", "Convo A", "Convo B/E", "Convo D", "Convo F", "Convo G", "Mason Street Deck Commuter", "U1 Lot", "U2 Lot", "U3 Lot", "U4 Lot", "U5 Lot", "Warsaw Ave Deck Level 2 commuter", "Warsaw Ave Deck Level 3", "Warsaw Ave Deck Level 4", "Warsaw Ave Deck Level 5", "U5 Lot", "Warsaw Ave Deck Level 2 commuter", "Warsaw Ave Deck Level 3", "Warsaw Ave Deck Level 4", "Warsaw Ave Deck Level 5"]
 )

	jmustatus3 = parkingApp.status("Visitor")
	assert (jmustatus2 ==["Parking Services provides visitors with parking permits at no charge during our normal business hours (7:00 AM - 5:00 PM Monday through Friday). Visitors who arrive at times other than those specified above should park in R1, R2, or R4 Lots and obtain a permit from Parking Services as soon as possible. (If a visitor receives a citation in the specified lots, they should contact Parking Services during business hours.) Visitors are not required to display permits after 3:00 PM on Friday through 7:00 AM Monday and may park in Commuter and Resident lots."]
)

	jmustatus4 = parkingApp.status("Blue")
	assert (jmustatus2 == ["1070 Virginia Avenue", "220 University Boulevard", "380 University Boulevard", "Alumni Drive", "Champions Drive Deck Level G", "Convo C", "D2 Lot", "D3 Lot", "D6 Lot", "D8 Lot", "E Lot", "G Lot", "L Lot", "P Lot", "R4 Lot IIHHS", "WMRA Lot"]
)

	jmustatus5 = parkingApp.status("Red")
	assert (jmustatus2 == ["1077 South Main Street", "131 West Grace Street", "A Lot", "B Lot", "C6 Lot SADAH", "Cantrell Ave Deck Level 2", "Cantrell Ave Deck Level 3", "Grace Street Deck Level 2", "Grace Street Deck Level 3", "Grace Street Deck Level 4", "Grace Street Deck Level 5", "Grace Street Deck Level 6", "Grace Street Deck Level 7", "I Lot", "Ice House Lot", "J lot", "K Lot", "M Lot", "Mason Street Deck Faculty/Staff", "Memorial Hall", "N3 Lot", "Q Lot East", "Q Lot North", "Q Lot West", "R8 Lot Faculty/Staff", "S Lot", "T Lot", "V Lot", "W Lot", "Warsaw Ave Deck Level 2 faculty/staff", "Warsaw Ave Deck Level G", "X Lot", "Y Lot", "Z Lot"]
)
