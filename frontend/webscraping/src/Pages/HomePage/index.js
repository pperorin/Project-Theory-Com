import { PageLayout, ProductCard } from "../../components";
import axios from "axios";
import { useState, useEffect } from "react";

const HomePage = () => {
  const [productcard, setProductcard] = useState([]);
  const [loading, setLoading] = useState(false);
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
                  <p>loading...</p>
                ) : (
                  productcard.map((product) => {
                    return <ProductCard product={product} />;
                  })
                )}
             
              {/* <div>
                        {loading&&loading2 ? (
                            <p>loading...</p>
                        ) : (
                            
                            productcard2.map((product2)=> {
                             return <ProductCard  product2={product2}  />;
                            })
                           
                            
                            
                            
                        )}
                        
                        
                        </div> */}
            </div>
         
        </div>
      </div>
    </PageLayout>
  );
};

export default HomePage;
