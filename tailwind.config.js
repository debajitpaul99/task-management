/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    ".templates/**/*.html", //Template at the project(root file) level
    "./**/templates/**/*.html" //Template inside app
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}

