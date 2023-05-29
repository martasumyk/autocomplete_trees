import React from 'react';
import './autocomplete-suggestions.css';
import SuggestionItem from "../suggestion-item";

interface Props {
    suggestions: string[],
    word: string,
    sentence: string
}

const AutocompleteSuggestions: React.FC<Props> = ({suggestions = [], word = "", sentence = ""}) => {
  return (
    <div id="suggestions">
      {
        !suggestions.length || suggestions[0] == ''?
          <small>{word ? `Unknown word ${word}` : "Start entering a word"}</small> :
          <ul id="suggestions-list">
            {
              suggestions.map((suggestion) =>
                <SuggestionItem
                  key={suggestion}
                  word={suggestion}
                  sentence={sentence}
                />)
            }
          </ul>
      }
    </div>
  );
};

export default AutocompleteSuggestions;
