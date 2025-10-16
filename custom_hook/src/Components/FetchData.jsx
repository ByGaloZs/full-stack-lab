import React from 'react'
import useFetch from './UseFetch'

const FetchData = () => {
  const [data] = useFetch('https://api.npoint.io/9045c260b1565daa9e15');
  console.log(data);
  
  return (
    <>
     <ul className='list_data_main'>
        <h1 className='usefetch_heading'>Use Fetch Custom Hook</h1>
     </ul>
    </>
  )
}

export default FetchData