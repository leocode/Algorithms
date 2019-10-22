# Who doesn't have a pair

The party is tonight. We've got a few hours left and I'm not sure that everybody is going to have somebody to talk to. People are paired by age. Here, take this list of ages of people who'll appear for sure. Please, if you find somebody without a pair, tell me how old they are so we can try to find somebody for them.

###Example of usage # 1:

aloneAtParty([25, 19, 21, 25, 21]) <br/>
Expected output # 1:

> The person alone is 19 years old.

###Example of usage # 2:

aloneAtParty([25, 19, 21, 25, 21, 19])<br/>
Expected output # 2:

> Everybody's got a pair.

### Run Script
run in the python folder:

Example1: python guestPairing/components/alone_at_party.py 25, 19, 21, 25, 21 <br/>
Example2: python guestPairing/components/alone_at_party.py 25, 19, 21, 25, 21, 19 <br/>

### Run Unit tests
run in the python folder:

pytest guestPairing/tests/alone_at_party_test.py