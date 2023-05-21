import React, { useState } from "react";
import "./autocomplete-page.css";
import logo from "./logo.svg";
import search from "./icon_search.svg";
import googlemic from "./googlemic.svg";
import AutocompleteSuggestions from "../../components/autocomplete-suggestions";

const AutocompletePage = () => {
  const [focused, setFocused] = useState(false);
  const [word, setWord] = useState("");

  const handleSubmit = (event: React.ChangeEvent<HTMLInputElement>) => {
    setWord(event.target.value)
    event.preventDefault();
    // Fetch data here using the word state
    fetch("/autocomplete", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ input: word }),
    })
      .then((response) => response.json())
      .then((data) => {
        console.log(data);
      })
      .catch((error) => {
        console.error("Error:", error);
      });
      console.log(11)
  };

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

        {focused && (
          <AutocompleteSuggestions
            suggestions={["banana", "bananaquit", "bananas", "banana's"]}
            word={word}
          />
        )}
      </div>
    </div>
  );
};

export default AutocompletePage;
