import React, { useState, useEffect } from "react";
import "./autocomplete-page.css";
import logo from "./logo.svg";
import search from "./icon_search.svg";
import googlemic from "./googlemic.svg";
import AutocompleteSuggestions from "../../components/autocomplete-suggestions";

const AutocompletePage = () => {
  const [focused, setFocused] = useState(false);
  const [word, setWord] = useState("");
  const [suggestions, setSuggestions] = useState([]);

  const handleSubmit = (event: React.ChangeEvent<HTMLInputElement>) => {
    setWord(event.target.value);
    event.preventDefault();
  };

  useEffect(() => {
    if (word) {
      fetch("/autocomplete", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ input: word }),
      })
        .then((response) => response.json())
        .then((data) => {
          const suggestionsArr = data.suggestions.split(", ");
          setSuggestions(suggestionsArr);
        })
        .catch((error) => {
          console.error("Error:", error);
        });
    }
  }, [word]);

  return (
    <div id="wrapper">
      <img src={logo} alt="logo" id="logo" />

      <div id="inputWrapper" className={focused ? "wrapper-focused" : ""}>
        <img src={search} alt="Search" id="search" />
        <form>
          <input
            id="input"
            type="text"
            autoComplete="off"
            spellCheck="false"
            role="combobox"
            aria-controls="matches"
            placeholder="Шукайте в Rabbits або поставте усім нам 100"
            aria-expanded="false"
            aria-live="polite"
            onClick={(e) => setFocused(true)}
            onChange={handleSubmit}
          />
        </form>
        <img src={googlemic} alt="mic" id="mic" />

        {focused && <AutocompleteSuggestions suggestions={suggestions} word={word} />}
      </div>
    </div>
  );
};

export default AutocompletePage;
