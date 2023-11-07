import React, { useState, useEffect } from 'react';

const Form = () => {

    const [data, setData] = useState([]);

    const fetchData = () => {
        fetch('http://127.0.0.1:8000/stockui/fetch_coin_data')
          .then((response) => response.json())
          .then((data) => setData(data))
          .catch((error) => console.error('Error:', error));
      };

    useEffect(() => {
        fetchData();
        const interval = setInterval(() => {
            fetchData();
            console.log("time")
          }, 3000);
          return () => clearInterval(interval);
      }, []);

    return (
      <table>
        <thead>
            <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Price</th>
            <th>1h %</th>
            <th>24h %</th>
            <th>7d %</th>
            <th>Market Cap</th>
            <th>Volume (24h)</th>
            <th>Circulating Supply</th>
            </tr>
        </thead>
        <tbody>
            <React.Fragment>
            {
                data.map(item => (
                    <tr key={item.id}>
                    <td>{item.id}</td>
                    <td>{item.name}</td>
                    <td>{item.price}</td>
                    <td>{item['1h_percent']}</td>
                    <td>{item['24h_percent']}</td>
                    <td>{item['7d_percent']}</td>
                    <td>{item.market_cap}</td>
                    <td>{item.volume_24h}</td>
                    <td>{item.circulating_supply}</td>
                  </tr>
                ))    
            }
            </React.Fragment>
        </tbody>
      </table>
    
    )
}

export default Form;