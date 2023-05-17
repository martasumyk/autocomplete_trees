import React from 'react';
import './autocomplete-suggestions.css';
import SuggestionItem from "../suggestion-item";

interface Props {
    suggestions: string[],
    word: string
}

const AutocompleteSuggestions: React.FC<Props> = ({suggestions = [], word = ""}) => {
  return (
    <div id="suggestions">
      {
        !suggestions.length ?
          <small>{word ? `Unknown word ${word}` : "Start entering a word"}</small> :
          <ul id="suggestions-list">
            {
              suggestions.map((suggestion) =>
                <SuggestionItem
                  key={suggestion}
                  word={suggestion}
                />)
            }
          </ul>
      }
    </div>
  );
};

export default AutocompleteSuggestions;
