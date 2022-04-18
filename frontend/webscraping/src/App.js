import { Routes, Route } from 'react-router-dom';

import { HomePage } from './Pages';
import  Stuffinfo  from'./components/PageLayout/stuffinfo'

function App() {
    return (
        <Routes>
            <Route path="/" element={<HomePage />} />
            <Route path="/stuffinfo/name" element={<Stuffinfo/>}/>
        </Routes>
    );
}

export default App;
