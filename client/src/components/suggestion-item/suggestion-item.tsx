import React from 'react';
import './suggestion-item.css';
import carrot from './carrot.svg'

interface Props {
  word: string
}
const SuggestionItem: React.FC<Props> = ({word}) => {
  return (
    <li className="suggestion-item">
      <a href={`https://www.google.com/search?q=${word.replace(' ', '+f')}`}>
        <img src={carrot} alt="Carrot" width={20}/>
        {word}
      </a>
    </li>
  );

};

export default SuggestionItem;
