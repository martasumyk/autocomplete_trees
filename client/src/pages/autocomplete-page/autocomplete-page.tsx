import React, { useState, useEffect } from "react";
import "./autocomplete-page.css";
import logo from "./logo.svg";
import search from "./icon_search.svg";
import googlemic from "./googlemic.svg";
import AutocompleteSuggestions from "../../components/autocomplete-suggestions";

const AutocompletePage = () => {
  const [focused, setFocused] = useState(false);
  const [word, setWord] = useState("");
  const [sentence, setSentence] = useState("")
  const [suggestions, setSuggestions] = useState([]);

  useEffect(() => {
    document.title = "Rabbits";
  }, []);

  const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    event.preventDefault();
    const {value} = event.target;

    setSentence(value);
    setWord(value.split(' ').at(-1) || '');
  };

  const submitHandler: React.FormEventHandler<HTMLFormElement> = (event) => {
    event.preventDefault();
    window.open(`https://www.google.com/search?q=${sentence}&lr=(-lang_ru)`, '_blank')!.focus();
  }

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
    } else {
      setSuggestions([]);
    }


  }, [word]);

  return (
    <div id="wrapper">
      <img src={logo} alt="logo" id="logo" />

      <div id="inputWrapper" className={focused ? "wrapper-focused" : ""}>
        <img src={search} alt="Search" id="search" />
        <form onSubmit={submitHandler}>
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
            onClick={() => setFocused(true)}
            onChange={handleChange}
          />
        </form>
        <img src={googlemic} alt="mic" id="mic" />

        {focused && <AutocompleteSuggestions suggestions={suggestions} word={word} sentence={sentence} />}
      </div>
    </div>
  );
};

export default AutocompletePage;
