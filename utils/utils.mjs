import {
  readFileSync,
} from 'fs';

/**
 * Read the input file.
 *
 * @param {string} path - The path to the input file
 * @returns {string[]} an array of each line
 */
export function readInput( path ) {
  const file = readFileSync(path, 'utf-8');
  return file.split(/(\n)/).filter(m => m.length > 1);
}
