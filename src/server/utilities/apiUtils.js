export const isStringNullOrEmpty = (source) => !source || source.trim() === "";

export const apiUrlFor = (master) => {
  return isStringNullOrEmpty(master) ? `/api/` : `/api/${master}`;
};
