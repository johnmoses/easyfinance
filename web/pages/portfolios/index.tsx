import { GetStaticProps, NextPage } from 'next';
import { addApolloState, initializeApollo } from '@/clients/apollo';
import Layout from '@/components/layout';
import { Tablify } from '@/modules/portfolios/Tablify';
import { Menus } from '@/modules/users/Menus';
// import { usePageAnalytics } from '@/hooks';

const PortfoliosTablePage: NextPage = () => {
  // usePageAnalytics();
  return (
    <Layout title='Portfolios'>
      <div className="float-left">
        <Menus />
      </div>
      <div className="flex justify-center items-center md:mt-5">
        <div className="flex max-w-md flex-col gap-2">
          <h5 className="mb-2 text-3xl font-bold text-gray-900 dark:text-white">
            Portfolios
          </h5>
        </div>
      </div>
      <Tablify />
    </Layout>
  );
};

export const getStaticProps: GetStaticProps = async () => {
  const apolloClient = initializeApollo();

  return addApolloState(apolloClient, {
    props: {},
  });
};

export default PortfoliosTablePage;