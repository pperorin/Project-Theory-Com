import { useSearchParams } from 'react-router-dom';

import axios from 'axios';
import { PageLayout, ProductCard } from '../../components';
import { useState, useEffect } from 'react';
import MockData from '../../components/MockData';
import FilterButton from '../../components/FilterButton';

const buttons = ['All', ...new Set(MockData.map((item) => item.Brand))];

const HomePage = () => {
    const [productcard, setProductcard] = useState([]);
    const [allSearchProduct, setAllSearchProduct] = useState([]);
    const [filteredProduct, setFilteredProduct] = useState([]);

    const [loading, setLoading] = useState(false);
    const [min, setMin] = useState(parseFloat(1));
    const [max, setMax] = useState(parseFloat(100000));

    const [searchParams] = new useSearchParams();
    const searchInput = searchParams.get('search');

    const filter = (button) => {
        if (button === 'All') {
            setFilteredProduct([]);
            return;
        }

        if (allSearchProduct.length > 0) {
            const filtered = allSearchProduct.filter((item) => item.Brand === button);
            setFilteredProduct(filtered);
        } else {
            const filtered = productcard.filter((item) => item.Brand === button);
            setFilteredProduct(filtered);
        }
    };

    const rangeFilter = async (min, max) => {
        if (allSearchProduct.length > 0) {
            const filtered = allSearchProduct.filter(
                (item) =>
                    parseFloat(item.Banana.replace(/,/g, '')) >= min && parseFloat(item.Banana.replace(/,/g, '')) <= max
            );
            filtered.concat(
                allSearchProduct.filter(
                    (item) =>
                        parseFloat(item.Ihavecpu.replace(/,/g, '')) >= min &&
                        parseFloat(item.Ihavecpu.replace(/,/g, '')) <= max
                )
            );
            setFilteredProduct(filtered);
        } else {
            const filtered = productcard.filter(
                (item) =>
                    parseFloat(item.Banana.replace(/,/g, '')) >= min && parseFloat(item.Banana.replace(/,/g, '')) <= max
            );
            filtered.concat(
                productcard.filter(
                    (item) =>
                        parseFloat(item.Ihavecpu.replace(/,/g, '')) >= min &&
                        parseFloat(item.Ihavecpu.replace(/,/g, '')) <= max
                )
            );

            setFilteredProduct(filtered);
        }
    };

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
            const dataFilter = ['Name', 'RegularName', 'Brand', 'Type'];
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
                <div className="col-span-1 mr-8">
                    <p className="text-xl">Filter</p>
                    <div>
                        <p className="text-lg">Price Range</p>
                        <div className="items-center">
                            <input
                                className="shadow appearance-none border rounded w-40 py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                                id="min"
                                type="text"
                                placeholder="min"
                                onChange={(e) => setMin(parseFloat(e.target.value))}
                            />
                            <input
                                className="shadow appearance-none border rounded w-40 py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                                id="max"
                                type="text"
                                placeholder="max"
                                onChange={(e) => setMax(parseFloat(e.target.value))}
                            />
                            <div>
                                <button
                                    type="button"
                                    data-mdb-ripple="true"
                                    data-mdb-ripple-color="light"
                                    onClick={() => rangeFilter(min, max)}
                                    className="inline-block px-6 py-2.5 bg-blue-600 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out m-2 "
                                >
                                    Apply
                                </button>
                            </div>
                        </div>
                    </div>
                    <div>
                        <p className="text-lg">Brands</p>
                        <FilterButton button={buttons} filter={filter} />
                    </div>
                </div>

                {loading && (
                    <div className="grid col-span-3 justify-center ">
                        <img
                            className=" "
                            src="https://cdn.dribbble.com/users/214929/screenshots/3154930/cat-jumping-aniamtion---gif.gif"
                            alt="this slowpoke moves"
                            width="400"
                        />
                        <div className="flex flex-row justify-center">
                            <svg
                                role="status"
                                className="h-8 w-8 animate-spin mr-2 text-gray-200 dark:text-gray-600 fill-blue-600"
                                viewBox="0 0 100 101"
                                fill="none"
                                xmlns="http://www.w3.org/2000/svg"
                            >
                                <path
                                    d="M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z"
                                    fill="currentColor"
                                />
                                <path
                                    d="M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z"
                                    fill="currentFill"
                                />
                            </svg>
                            <div>loading...</div>
                        </div>
                    </div>
                )}
                <div className="col-span-3">
                    <div className="grid grid-cols-3 gap-4">
                        {!loading &&
                            !searchInput &&
                            filteredProduct.length === 0 &&
                            productcard.map((product, index) => {
                                return <ProductCard product={product} key={index} />;
                            })}
                        {!loading && searchInput && allSearchProduct.length === 0 && <p>Not Found...</p>}
                        {!loading && filteredProduct.length === 0 && <p>Not Found...</p>}
                        {!loading &&
                            allSearchProduct.length > 0 &&
                            filteredProduct.length === 0 &&
                            allSearchProduct.map((product, index) => {
                                return <ProductCard product={product} key={index} />;
                            })}
                        {!loading &&
                            filteredProduct.length > 0 &&
                            filteredProduct.map((product, index) => {
                                return <ProductCard product={product} key={index} />;
                            })}
                    </div>
                </div>
            </div>
        </PageLayout>
    );
};

export default HomePage;
