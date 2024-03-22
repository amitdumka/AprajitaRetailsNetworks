import React, { PureComponent } from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
//import { Test } from './Banks.styles';

class Banks extends PureComponent { 
  constructor(props) {
    super(props);

    this.state = {
      hasError: false,
    };
  }

  componentWillMount = () => {
    console.log('Banks will mount');
  }

  componentDidMount = () => {
    console.log('Banks mounted');
  }

  componentWillReceiveProps = (nextProps) => {
    console.log('Banks will receive props', nextProps);
  }

  componentWillUpdate = (nextProps, nextState) => {
    console.log('Banks will update', nextProps, nextState);
  }


  componentDidUpdate = () => {
    console.log('Banks did update');
  }

  componentWillUnmount = () => {
    console.log('Banks will unmount');
  }

  render () {
    if (this.state.hasError) {
      return <h1>Something went wrong.</h1>;
    }
    return (
      <div className="BanksWrapper">
        Test content
      </div>
    );
  }
}

Banks.propTypes = {
  // bla: PropTypes.string,
};

Banks.defaultProps = {
  // bla: 'test',
};

const mapStateToProps = state => ({
  // blabla: state.blabla,
});

const mapDispatchToProps = dispatch => ({
  // fnBlaBla: () => dispatch(action.name()),
});

export default connect(
  mapStateToProps,
  mapDispatchToProps,
)(Banks);
