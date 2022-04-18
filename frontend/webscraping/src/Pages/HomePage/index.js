import {PageLayout} from '../../components'

const HomePage = () => {
    return (
        <PageLayout>
            <h1 className="text-center text-3xl font-bold underline">This is HomePage</h1>
            <a href='/stuffinfo/name'><h2>test</h2></a>
        </PageLayout>
    );
}

export default HomePage