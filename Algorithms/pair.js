const tmp = [1, 2, 3, 4, 5, 4, 3, 2, 1];
const tmpAnswer = 5

const aloneAtParty = (tmp) => {
  const a = tmp.reduce((acc, e) => {return acc+e}, 0);
  const b = [...new Set(tmp)].reduce((acc, e) => {return acc+e}, 0);
  return b-(a-b);
};

console.log(tmpAnswer === aloneAtParty(tmp));

