import { Link, useSearchParams } from 'react-router-dom';
import { useState, useEffect } from 'react';
import './NavigationStyle.css';
import Dropdown from './Dropdown';
import { navItems } from './NavItems';

const NavigationBar = () => {
    const [dropdown, setDropdown] = useState(false);
    const [search, setSearch] = useState('');
    const [searchParams, setSearchParams] = new useSearchParams();
    const searchKeyword = searchParams.get('search');

    const onEnterSearch = () => {
        setSearchParams({ search });
    };

    useEffect(() => {
        if (searchKeyword) {
            setSearch(searchKeyword);
        } else {
            setSearch('');
        }
    }, [searchKeyword]);

    return (
        <nav className="bg-white border-gray-200 px-2 sm:px-4 py-2.5 dark:bg-gray-800">
            <div className="container flex flex-wrap justify-between items-center mx-auto">
                <a href="/" className="flex items-center">
                    <span className="self-center text-xl font-semibold whitespace-nowrap dark:text-white">HOME</span>
                </a>
                <a href="https://github.com/pperorin/Project-Theory-Com" className="flex items-center">
                    <span className="self-center text-xl font-semibold whitespace-nowrap dark:text-white">GITHUB</span>
                </a>
                <div className="Bars">
                    <ul className="nav-items">
                        {navItems.map((item) => {
                            if (item.title === 'Home') {
                                return (
                                    <li
                                        key={item.id}
                                        className={item.cName}
                                        onMouseEnter={() => setDropdown(true)}
                                        onMouseLeave={() => setDropdown(false)}
                                    >
                                        <Link to={item.path}>{item.icon}</Link>
                                        {dropdown && <Dropdown />}
                                    </li>
                                );
                            }
                            return (
                                <li key={item.id} className={item.cName}>
                                    <Link to={item.path}>{item.icon}</Link>
                                </li>
                            );
                        })}
                    </ul>
                </div>
                <div className="flex md:order-2">
                    <div className="hidden relative mr-3 md:mr-0 md:block">
                        <div className="flex absolute inset-y-0 left-0 items-center pl-3 pointer-events-none">
                            <svg
                                className="w-5 h-5 text-gray-500"
                                fill="currentColor"
                                viewBox="0 0 20 20"
                                xmlns="http://www.w3.org/2000/svg"
                            >
                                <path
                                    fillRule="evenodd"
                                    d="M8 4a4 4 0 100 8 4 4 0 000-8zM2 8a6 6 0 1110.89 3.476l4.817 4.817a1 1 0 01-1.414 1.414l-4.816-4.816A6 6 0 012 8z"
                                    clipRule="evenodd"
                                ></path>
                            </svg>
                        </div>
                        <input
                            type="text"
                            className="block p-2 pl-10 w-full text-gray-900 bg-gray-50 rounded-lg border border-gray-300 sm:text-sm focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                            placeholder="ค้นหาสินค้า..."
                            value={search}
                            onChange={(e) => setSearch(e.target.value)}
                            onKeyPress={(event) => {
                                if (event.key === 'Enter') {
                                    onEnterSearch();
                                }
                            }}
                        />
                    </div>
                </div>
            </div>
        </nav>
    );
};

export default NavigationBar;
