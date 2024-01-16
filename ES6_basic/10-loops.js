export default function appendToEachArrayValue(array, appendString) {
  var newArray = [];
  for (var value of array) {
    newArray.push(appendString + value);
  }
  return newArray;
}