/** @type {import('tailwindcss').Config} */
const defaultTheme = require("tailwindcss/defaultTheme");

module.exports = {
  darkMode: "class",
  content: ["./src/static/**/*.{html,js,ts,jsx,tsx,j2,jinja2}"],
  plugins: [
    require("@tailwindcss/forms"),
    require("@tailwindcss/typography"),
    require("@tailwindcss/aspect-ratio"),
  ],
  theme: {
    extend: {
      colors: {
        "litestar-gold": "#EDB641",
        "litestar-blue": "#202235",
        "litestar-yellow": "#FFD480",
        "litestar-gray": "#DCDFE4",
        "litestar-white": "#ffffff",
      },
    },
  },
};
