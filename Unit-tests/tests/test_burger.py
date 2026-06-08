import pytest
from unittest.mock import Mock
from praktikum.burger import Burger

class TestBurger:

    #Проверяем, что булочка сэтится.
    def test_set_buns(self):
        burger = Burger()
        mock_bun = Mock()
        burger.set_buns(mock_bun)
        assert burger.bun is mock_bun
    
    #Проверяем, что ингредиент добавляется.
    def test_add_ingredient(self):
        burger = Burger()
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)
        assert mock_ingredient in burger.ingredients
        assert len(burger.ingredients) == 1

    #Проверяем удаление ингредиента по индексу через параметризацию (инициализируется количество ингредиентов, индекс ингредиента для удаления, ожидаемое количество оставшихся ингредиентов)
    @pytest.mark.parametrize(
        "initial_ingredients_count, index_to_remove, expected_count",
        [(3, 1, 2),
         (3, 2, 2),
         (3, 0, 2),
         (1, 0, 0)
        ])
    def test_remove_ingredient(self, initial_ingredients_count, index_to_remove, expected_count):
        burger = Burger()
        mock_ingredients = [Mock() for _ in range(initial_ingredients_count)]
        for ing in mock_ingredients:
            burger.add_ingredient(ing)
        burger.remove_ingredient(index_to_remove)
        assert len(burger.ingredients) == expected_count

    #Проверяем перемещение ингредиента по индексу через параметризацию (инициализируется позиция ингридиента в списке из трёх и двух ингредиентов). 
    # Проверяется ожидаемая позиция перемещённого ингредиента. Моки создаются динамически.
    @pytest.mark.parametrize(
        "from_index, to_index, expected_order",
        [
            pytest.param(2, 0, [2, 0, 1], id="move_last_to_start"),   # 1. 3 элемента: Перемещение с конца в начало
            pytest.param(0, 2, [1, 2, 0], id="move_first_to_end"),    # 2. 3 элемента: Перемещение с начала в конец
            pytest.param(0, 1, [1, 0, 2], id="move_start_to_middle"), # 3. 3 элемента: Перемещение с начала в середину
            pytest.param(2, 1, [0, 2, 1], id="move_end_to_middle"),   # 4. 3 элемента: Перемещение с конца в середину
            pytest.param(1, 1, [0, 1, 2], id="move_to_same_position"),# 5. 3 элемента: Перемещение "на себя" (ничего не меняется)
            pytest.param(0, 0, [0], id="single_element"),             # 6. 2 элемента: Перемещение "на себя" (ничего не меняется)
            pytest.param(1, 0, [1, 0], id="swap_two_elements"),       # 7. 2 элемента: Меняютя местами
        ]
    )
    def test_move_ingredient(self, from_index, to_index, expected_order):
        burger = Burger()
        if expected_order:
            max_index = max(expected_order)
            mock_ingredients = [Mock() for _ in range(max_index + 1)]
            for ing in mock_ingredients:
                burger.add_ingredient(ing)
        else:
            mock_ingredients = []
        burger.move_ingredient(from_index, to_index)
        expected_ingredients_order = [mock_ingredients[i] for i in expected_order]
        assert burger.ingredients == expected_ingredients_order     

    #Проверяем расчет итоговой цены при разных комбинациях булочки и ингредиентов.
    @pytest.mark.parametrize(
        "bun_price, ingredients_prices, expected_total",
        [
        (150.0, [], 300.0),                     # Булочка без начинки
        (100.0, [50.0], 250.0),                 # Булочка с одним ингредиентом
        (200.0, [100.0, 150.0], 650.0),         # Булочка с несколькими ингредиентами
        (500.0, [300.0, 400.0, 250.0], 1950.0), # Дорогая булочка и дорогие ингредиенты
        ]
    )
    def test_get_price(self, bun_price, ingredients_prices, expected_total):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_price.return_value = bun_price
        burger.set_buns(mock_bun)
        for price in ingredients_prices:
            mock_ingredient = Mock()
            mock_ingredient.get_price.return_value = price
            burger.add_ingredient(mock_ingredient)
        assert burger.get_price() == expected_total

    # Проверяем формирование чека (строки и стоимости бургера)
    def test_get_receipt(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_name.return_value = "Black Bun"
        mock_bun.get_price.return_value = 150.0
        burger.set_buns(mock_bun)

        mock_ing1 = Mock()
        mock_ing1.get_type.return_value = "SAUCE"
        mock_ing1.get_name.return_value = "Ketchup"
        mock_ing1.get_price.return_value = 150.0
        burger.add_ingredient(mock_ing1)

        expected_receipt = (
            "(==== Black Bun ====)\n"
            "= sauce Ketchup =\n"
            "(==== Black Bun ====)\n"
            "\n" 
            "Price: 450.0"
        )
        
        assert burger.get_receipt() == expected_receipt
