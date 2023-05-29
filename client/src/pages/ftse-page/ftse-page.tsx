import React, { useEffect, useState } from 'react';
import './ftse-page.css';
import { Link } from 'react-router-dom';

  
const FTSEPage: React.FC = () => {
  const [text, setText] = useState(`Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed tincidunt ornare consectetur. Nulla lobortis in libero ac luctus. Morbi et lobortis nunc, a imperdiet felis. Maecenas urna neque, vehicula id enim sit amet, faucibus commodo ex. Integer nec turpis eros. Quisque ac ligula sit amet est tristique condimentum eget sodales purus. In mattis purus nibh, id cursus eros venenatis vel. Nulla vel vehicula diam. Fusce purus lacus, cursus non elit ac, tincidunt molestie turpis. Etiam faucibus nisl neque, non facilisis tellus vulputate dictum. Vestibulum efficitur eleifend lacus, quis cursus tellus. Nullam sit amet venenatis neque. Quisque ex mi, scelerisque vel varius in, efficitur in nunc.`);
  const [search, setSearch] = useState('');
  const [positions, setPositions] = useState<number[]>([]);

  useEffect(() => {
    if (text && search) {
      fetch("/fulltextsearch", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({text, search}),
      })
        .then((response) => response.json())
        .then((data) => {
          setPositions(data);
        })
        .catch((error) => console.error("Error:", error));
    } else {
      setPositions([]);
    }
  }, [text, search])

  return (
    <>
      <p className='link-wrapper'><Link to='/' className='link'>Autocomplete</Link></p>

      <div className="wrapper">
        <div className="inputs">
          <div className="centerForm">
              <textarea 
                cols={60} rows={8} 
                maxLength={500} 
                className="text-area"
                placeholder="Enter your text" 
                onChange={(event) => setText(event.target.value)}  
                defaultValue={text}
              ></textarea>

              <input
                value={search}
                className="text-area"
                placeholder="Enter phrase to search"
                onChange={(event) => setSearch(event.target.value)}
              />
            </div>
          </div>

        <div className="text">
          <pre>
            {
              positions.length ? 
                positions.map((position, i) => {
                  if (i === positions.length - 1) {
                    return <React.Fragment key={position}>
                      <span>{text.substring(positions[i - 1] + search.length, position)}</span>
                      <mark>{text.substring(position, position + search.length)}</mark>
                      <span>{text.substring(position + search.length, text.length)}</span>
                    </React.Fragment>
                  }

                  if (i === 0) {
                    return <React.Fragment key={position}>
                      <span>{text.substring(0, position)}</span>
                      <mark>{text.substring(position, position + search.length)}</mark>
                      </React.Fragment>;
                  }
                  
                  return <React.Fragment key={position}>
                    <span>{text.substring(positions[i - 1] + search.length, position)}</span>
                    <mark>{text.substring(position, position + search.length)}</mark>
                  </React.Fragment>;
                }) :
                text
            }
          </pre>
        </div>
      </div>
    </>
  );
};

export default FTSEPage;
