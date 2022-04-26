import { useSearchParams } from 'react-router-dom'

import axios from "axios";
import { PageLayout, ProductCard } from "../../components";
import { useState, useEffect } from "react";

const HomePage = () => {
  const [productcard, setProductcard] = useState([]);
  const [loading, setLoading] = useState(false);

  const [searchParams] = new useSearchParams();
  const searchInput = searchParams.get('search')

  useEffect(() => {
    const getdata = async () => {
      try {
        setLoading(true);
        const data = await axios.get(
          "https://theorybackend.herokuapp.com/keyboard"
        );
        const data2 = await axios.get(
          "https://theorybackend.herokuapp.com/headgear"
        );
        setProductcard([...data.data, ...data2.data]);
        
        // setProductcard(keyboard=>[...keyboard,data2.data])
        // setProductcard2(data2.data);
      } catch (err) {
        // toast.error(err.response.data.messsage);
      }
      setLoading(false);
    };
    // const getdata2 = async () => {
    //     try {
    //       setLoading2(true);

    //       const data2 = await axios.get("https://theorybackend.herokuapp.com/headgear")

    //       setProductcard(data2.data);

    //       console.log(productcard2)
    //     } catch (err) {
    //       // toast.error(err.response.data.messsage);
    //     }
    //     setLoading2(false);
    //   };
    getdata();
    // getdata2();
  }, []);


  return (
    <PageLayout>
      <div className="grid grid-cols-4">
        <div className="col-span-1 border-4 border-sky-500 mr-8">
          Filter panel
        </div>
        <div className="col-span-3">
          
        <div className="grid grid-cols-3 gap-4">
              
                {loading ? (
                  
                 
                  <img className=" " src="https://cdn.dribbble.com/users/214929/screenshots/3154930/cat-jumping-aniamtion---gif.gif" alt="this slowpoke moves"  width="400" />
                  
                )
              
                : (
                  productcard.map((product,index) => {
                    return <ProductCard product={product} key={index}/>;
                  })
                )}
             
            </div>
         
        </div>
      </div>
    </PageLayout>
  );
};

export default HomePage;
