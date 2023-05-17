import React, {useState} from "react";
import './autocomplete-page.css';
import logo from './logo.svg'
import search from './icon_search.svg'
import googlemic from './googlemic.svg'
import AutocompleteSuggestions from "../../components/autocomplete-suggestions";

const AutocompletePage = () => {
    const [focused, setFocused] = useState(false)
    const [word, setWord] = useState("")


    return (
        <div id="wrapper">
            <img src={logo} alt="logo" id="logo" />

            <div id="inputWrapper" className={focused ? "wrapper-focused" : ""}>
                <img src={search} alt="Search" id="search"/>
                <input id="input" type="text" autoComplete="off" spellCheck="false" role="combobox" aria-controls="matches"
                   placeholder="Шукайте в Rabbits або поставте усім нам 100" aria-expanded="false" aria-live="polite"
                    onClick={() => setFocused(true)}
                    onChange={(event) => setWord(event.target.value)}
                />
                <img src={googlemic} alt="mic" id="mic"/>

                {focused && <AutocompleteSuggestions suggestions={['banana', 'bananaquit', 'bananas', "banana's"]} word={word} />}
            </div>
        </div>
    );
}

export default  AutocompletePage;