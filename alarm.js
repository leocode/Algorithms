const alarm = (time) => {
  const convertHourToMinutes = (hours, minutes) => {
    return (parseInt(hours) * 60 + parseInt(minutes));
  }

  const MINUTES_IN_ONE_DAY = 1440

  const [alarmHours, alarmMinutes] = time.split(':');
  const currentDate = new Date();
  const currentHour = currentDate.getHours();
  const currentMinute = currentDate.getMinutes();

  const currentTimeInMins = convertHourToMinutes(currentHour, currentMinute);
  const alarmTimeInMins = convertHourToMinutes(alarmHours, alarmMinutes);
  let result;

  if(alarmTimeInMins < currentTimeInMins) {
    result = MINUTES_IN_ONE_DAY - currentTimeInMins + alarmTimeInMins;
  } else {
    result = alarmTimeInMins - currentTimeInMins;
  }

  let answerHours = Math.floor(result/60)
  let answerMinutes = result%60;

  console.log(answerHours, answerMinutes);
}

alarm('23:30');
