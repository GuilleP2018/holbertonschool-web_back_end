export default function appendToEachArrayValue(array, appendString) {
  for (var [idx, value] of array.entries()) {
    array[idx] = appendString + value;
  }

  return array;
}