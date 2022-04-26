import { useSearchParams } from 'react-router-dom';

import axios from 'axios';
import { PageLayout, ProductCard } from '../../components';
import { useState, useEffect } from 'react';

const HomePage = () => {
    const [productcard, setProductcard] = useState([]);
    const [allFetchProduct, setAllfetchProduct] = useState([]);
    const [allSearchProduct, setAllSearchProduct] = useState([]);
    const [loading, setLoading] = useState(false);

    const [searchParams] = new useSearchParams();
    const searchInput = searchParams.get('search');

    useEffect(() => {
        const getdata = async () => {
            try {
                setLoading(true);
                const keyboradData = await axios.get('https://theorybackend.herokuapp.com/keyboard');
                const headgearData = await axios.get('https://theorybackend.herokuapp.com/headgear');
                const mouseData = await axios.get('https://theorybackend.herokuapp.com/mouse');
                setProductcard([...keyboradData.data, ...headgearData.data, ...mouseData.data]);
            } catch (err) {
                alert(err.response.data.messsage);
            }
            setLoading(false);
        };
        getdata();
    }, []);

    useEffect(() => {
        if (searchInput && !loading) {
            const dataFilter = ['Name', 'RegularName', 'Brand'];
            const data = productcard.filter((item) => {
                return dataFilter.some((filter) => {
                    if (item[filter]) {
                        return item[filter].toString().toLowerCase().indexOf(searchInput.toLowerCase()) > -1;
                    }
                    return null;
                });
            });
            setAllSearchProduct(data);
        } else if (!searchInput && !loading) {
            setAllSearchProduct([]);
        }
    }, [searchInput, loading, productcard]);

    return (
        <PageLayout>
            <div className="grid grid-cols-4">
                <div className="col-span-1 border-4 border-sky-500 mr-8">Filter panel</div>
                <div className="col-span-3">
                    <div className="grid grid-cols-3 gap-4">
                        {loading && (
                            <img
                                className=" "
                                src="https://cdn.dribbble.com/users/214929/screenshots/3154930/cat-jumping-aniamtion---gif.gif"
                                alt="this slowpoke moves"
                                width="400"
                            />
                        )}
                        {!loading &&
                            !searchInput &&
                            productcard.map((product, index) => {
                                return <ProductCard product={product} key={index} />;
                            })}
                        {!loading && searchInput && allSearchProduct.length === 0 && <p>Not Found...</p>}
                        {!loading &&
                            allSearchProduct.length > 0 &&
                            allSearchProduct.map((product, index) => {
                                return <ProductCard product={product} key={index} />;
                            })}
                    </div>
                </div>
            </div>
        </PageLayout>
    );
};

export default HomePage;
