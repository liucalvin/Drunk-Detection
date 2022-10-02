/**
 * Converts an image from a user's local computer to a @type {File} object.
 * @see https://stackoverflow.com/a/38935990
 */
export function dataURLtoFile(dataurl, filename) {
  var arr = dataurl.split(","),
    mime = arr[0].match(/:(.*?);/)[1],
    ext = mime.split("/")[1],
    bstr = atob(arr[1]),
    n = bstr.length,
    u8arr = new Uint8Array(n);
  while (n--) {
    u8arr[n] = bstr.charCodeAt(n);
  }
  filename = `${filename}.${ext}`;
  return new File([u8arr], filename, { type: mime });
}
