export default function appendToEachArrayValue(array, appendString) {
  var newArray = [];
  for (const value of array) {
    newArray.push(appendString + value);
  }
  return newArray;
}