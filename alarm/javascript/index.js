const setAlarm = wakeUpTime => {
  const [hour, minute] = wakeUpTime.split(":");
  const currentTime = new Date();
  const currentHour = +currentTime.getHours();
  const minutes = Math.abs(currentTime.getMinutes() - minute);

  let hours = 0;
  if (currentHour > hour) {
    hours = 24 - currentHour + +hour;
  } else {
    hours = +hour - currentHour;
  }

  const hourPrefix = hours !== 1 ? "s" : "";
  const minutesPrefix = minutes !== 1 ? "s" : "";
  console.log(
    `I will have been sleeping for ${hours} hour${hourPrefix} and ${minutes} minute${minutesPrefix}.`
  );
};

setAlarm("13:45");
setAlarm("5:01");
setAlarm("00:15");
