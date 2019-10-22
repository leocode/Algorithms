const aloneAtParty = arr => {
  const sortedArr = arr.sort((a,b) => a - b);
  let response = `Everybody's got a pair.`

  sortedArr.map((item, index) => {
    const prevItem = sortedArr[index - 1];
    const nextItem = sortedArr[index + 1];

    (item !== prevItem && item !== nextItem)
      ? response = `The person alone is ${item} years old.`
      : null
  });
  console.log(response);
};

const arr = [26,28,23,12,15,15,93,93,26,28,12,23];
aloneAtParty(arr);