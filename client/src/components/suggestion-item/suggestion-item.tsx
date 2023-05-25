import React from 'react';
import './suggestion-item.css';
import carrot from './carrot.svg'

interface Props {
  word: string,
  sentence: string
}
const SuggestionItem: React.FC<Props> = ({word, sentence}) => {
  const length = sentence.split(' ').length;
  const search = sentence.split(' ').slice(0, -1).join(" ") + " " + word;

  return (
    <li className="suggestion-item">
      <a href={`https://www.google.com/search?q=${search}`}>
        <img src={carrot} alt="Carrot" width={20}/>
        {length > 1 ? '...' : ''}{word}
      </a>
    </li>
  );

};

export default SuggestionItem;
