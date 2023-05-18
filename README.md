# Podomarket
<div align='center'>
  <img width="80%" src="https://user-images.githubusercontent.com/113345693/220639537-c038b318-c9c1-4f46-a351-f1520a01e6e4.gif" />
 </div>

# Description
포도마켓은 중고 물품 거래 웹사이트이다. 상품 이름, 가격, 상태, 사진 등을 포함한 게시글을 올릴 수 있고 물품 거래를 할 수 있다.


# Environment
- Django
- Python
- HTML
- CSS


# Comment
- Django의 allauth 패키지를 사용해 유저 기능을 구현했다.
- allauth는 유저 기능에 필요한 URL패턴, 뷰, 폼 등을 제공해 보다 편리하게 구현할 수 있다.
- 다만 allauth가 제공하는 setting들이 매우 다양해 적절한 기능을 찾는 데 어려움이 있었다.
- 댓글 기능을 추가하였다. 게시글에 댓글을 작성할 수 있고, 본인이 작성한 댓글에 대해 수정, 삭제 할 수 있다.
- 게시글 좋아요, 댓글 좋아요 기능을 추가하였다.
- 유저 팔로잉 기능을 추가하였다.
- 좋아요 한 게시글만 모아볼 수 있는 위시리스트 기능을 구현하였다.
- 팔로잉한 유저들의 게시글만 모아볼 수 있는 모아보기 기능을 구현하였다.
