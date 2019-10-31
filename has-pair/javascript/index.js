const aloneAtParty = partyGuests => {
  const alone = partyGuests.reduce((acc, guest) => acc ^ guest, 0);
  if (!alone) {
    console.log("Everybody's got a pair.");
  } else {
    console.log(`The person alone is ${alone} years old.`);
  }
};

aloneAtParty([25, 19, 21, 25, 21, 19]);
aloneAtParty([25, 19, 21, 25, 21]);
