const convertTime = (motiveTime, clockStop, convertToMs, convertToHours) => {
    const convertedMotive = motiveTime.split(":");
    const convertedClockStop = clockStop.split(":");
    const msMotive = convertToMs(convertedMotive[0],convertedMotive[1]);
    const msClockStop = convertToMs(convertedClockStop[0],convertedClockStop[1]);
    const maxNum = Math.max(...[msMotive,msClockStop]);
    const minNum = Math.min(...[msClockStop,msMotive]);
    if(maxNum && minNum > 0) {
        const getFullTimeOfSleep = (maxNum - minNum);
        return convertToHours(getFullTimeOfSleep);
    }
}
const getMiliseconds = (h,m) => {
    return ((h*60*60+m*60)*1000);
}

function timeConversion(millisec) {

    const seconds = (millisec / 1000).toFixed(1);
    const minutes = (millisec / (1000 * 60)).toFixed(1);
    const hours = (millisec / (1000 * 60 * 60)).toFixed(1);
    const days = (millisec / (1000 * 60 * 60 * 24)).toFixed(1);

    if (seconds < 60) {
        return seconds + " Sec";
    } else if (minutes < 60) {
        return minutes + " Min";
    } else if (hours < 24) {
        return hours + " Hrs";
    } else {
        return days + " Days"
    }
}
console.log(convertTime("5:15", "21:10", getMiliseconds,timeConversion));